import subprocess
import unittest
import uuid
from pathlib import Path

import defectdojo_api_generated
from defectdojo_api_generated import DefectDojo
from defectdojo_api_generated.models.product_request import ProductRequest
from defectdojo_api_generated.models.product_type_request import ProductTypeRequest

DOJO_SCRIPTS = Path(__file__).parent.parent.parent / 'support' / 'integration'
DATA_DIR = Path(__file__).parent.parent / 'data'


# @unittest.skipUnless(os.getenv('DD_INTEGRATION_TESTS'), 'Integration tests not enabled')
class Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        return
        subprocess.check_call([DOJO_SCRIPTS / 'run_dojo.sh'])

    @classmethod
    def tearDownClass(cls):
        return
        subprocess.check_call([DOJO_SCRIPTS / 'stop_dojo.sh'])

    def client(self, url='http://127.0.0.1:8080', user='admin', password='admin'):
        return DefectDojo(base_url=url, auth=(user, password))

    def test_login(self):
        c = self.client(password='wrong')
        with self.assertRaises(defectdojo_api_generated.exceptions.ForbiddenException):
            c.user_profile_api.user_profile_retrieve()

    def _create_product(self, skip_if_fail=True):
        c = self.client()
        uniq = str(uuid.uuid4())
        try:
            pt = c.product_types_api.product_types_create(product_type_request=ProductTypeRequest(name=f'Test {uniq}'))
            return c.products_api.products_create(
                product_request=ProductRequest(name=f'Product {uniq}', description='test', prod_type=pt.id)
            )
        except Exception:
            if skip_if_fail:
                self.skipTest('product creation failed')
            else:
                raise

    def test_create_product(self):
        p = self._create_product(skip_if_fail=False)
        self.assertEqual(p.description, 'test')

    def test_reimport_scan(self):
        c = self.client()
        product = self._create_product()
        report = c.reimport_scan_api.reimport_scan_create(
            scan_type='Semgrep JSON Report',
            product_name=product.name,
            engagement_name='Test',
            auto_create_context=True,
            file=str(DATA_DIR / 'semgrep_report.json'),
        )
        self.assertEqual(report.statistics.after.total.total, 3)
