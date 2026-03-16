import os
import subprocess
import unittest
import uuid
from pathlib import Path

import pydantic

import defectdojo_api_generated
from defectdojo_api_generated import DefectDojo
from defectdojo_api_generated.models import AddNewNoteOptionRequest, ProductRequest, ProductTypeRequest

DOJO_SCRIPTS = Path(__file__).parent.parent.parent / 'support' / 'integration'
DATA_DIR = Path(__file__).parent.parent / 'data'

# Run `run_dojo.sh` manually (and stop after), set this one to True and then you can run individual tests here quickly
_PARTIAL_RUN = False


@unittest.skipUnless(_PARTIAL_RUN or os.getenv('DD_INTEGRATION_TESTS'), 'Integration tests not enabled')
class Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        if not _PARTIAL_RUN:
            subprocess.check_call([DOJO_SCRIPTS / 'run_dojo.sh'])

    @classmethod
    def tearDownClass(cls):
        if not _PARTIAL_RUN:
            subprocess.check_call([DOJO_SCRIPTS / 'stop_dojo.sh'])

    def setUp(self):
        self.client = self._client()

    def _client(self, url='http://127.0.0.1:8080', user='admin', password='admin'):
        return DefectDojo(base_url=url, auth=(user, password))

    def test_login(self):
        c = self._client(password='wrong')
        with self.assertRaises(defectdojo_api_generated.exceptions.ForbiddenException):
            c.user_profile_api.retrieve()

    def _create_product(self):
        uniq = str(uuid.uuid4())
        pt = self.client.product_types_api.create(product_type_request=ProductTypeRequest(name=f'Test {uniq}'))
        return self.client.products_api.create(
            product_request=ProductRequest(name=f'Product {uniq}', description='test', prod_type=pt.id)
        )

    def test_create_product(self):
        product = self._create_product()
        self.assertEqual(product.description, 'test')

    def _reimport_scan(self):
        product = _skip_if_fail(self._create_product)
        report = self.client.reimport_scan_api.create(
            scan_type='Semgrep JSON Report',
            product_name=product.name,
            engagement_name='Test',
            auto_create_context=True,
            file=str(DATA_DIR / 'semgrep_report.json'),
        )
        return report

    def test_reimport_scan(self):
        report = self._reimport_scan()
        self.assertEqual(report.statistics.after.total.total, 3)

    def DISABLED_test_bad_api_model_definitions(self):
        """This a test to assert issue https://github.com/fopina/defectdojo-api-generated/issues/39"""
        # this has been disabled as https://github.com/fopina/defectdojo-api-generated/pull/45 made all properties optional
        # this can be re-introduced by removing `tweak_required` from `tweak_openapi.py`
        report = _skip_if_fail(self._reimport_scan)
        page = self.client.findings_api.list(test=report.test)
        self.assertEqual(page.count, 3)
        self.assertEqual(page.results[0].notes, [])
        try:
            self.client.findings_api.notes_create(page.results[0].id, AddNewNoteOptionRequest(entry='ehlo'))
            self.fail('WAS THIS FIXED??')
        except pydantic.ValidationError as exc:
            # this is what SHOULD NOT happen
            # note was created (because note_type is NOT required) but parsing the resulting Note model fails
            self.assertIn(
                """note_type\n  Input should be a valid dictionary or instance of NoteType [type=model_type, input_value=None, input_type=NoneType]""",
                str(exc),
            )

        try:
            page = self.client.findings_api.list(test=report.test)
            self.fail('WAS THIS FIXED??')
        except pydantic.ValidationError as exc:
            # same for simply listing findings, all broken...
            self.assertIn(
                """note_type\n  Input should be a valid dictionary or instance of NoteType [type=model_type, input_value=None, input_type=NoneType]""",
                str(exc),
            )

    def test_bad_api_model_definitions_fixed(self):
        """
        This test relates to DISABLED_test_bad_api_model_definitions as it asserts the OPPOSITE
        This is to ensure the issue no longer happens given all properties were made optional
        """
        report = _skip_if_fail(self._reimport_scan)
        page = self.client.findings_api.list(test=report.test)
        self.assertEqual(page.count, 3)
        self.assertEqual(page.results[0].notes, [])
        note = self.client.findings_api.notes_create(page.results[0].id, AddNewNoteOptionRequest(entry='ehlo'))
        self.assertEqual(note.note_type, None)

    def test_iterator(self):
        report = _skip_if_fail(self._reimport_scan)
        result = next(self.client.findings_api.list_iterator(test=report.test))
        self.assertEqual(result.page.count, 3)
        self.assertEqual(result.result.title, 'java.lang.security.audit.cbc-padding-oracle.cbc-padding-oracle')


def _skip_if_fail(test_dependency):
    try:
        return test_dependency()
    except Exception:
        raise unittest.SkipTest('dependency failed')
