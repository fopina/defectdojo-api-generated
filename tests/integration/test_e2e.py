import os
import subprocess
import unittest
import uuid
from pathlib import Path

import defectdojo_api_generated
from defectdojo_api_generated import DefectDojo
from defectdojo_api_generated.models.product_request import ProductRequest
from defectdojo_api_generated.models.product_type_request import ProductTypeRequest

DOJO_SCRIPTS = Path(__file__).parent.parent.parent / 'support' / 'integration'


@unittest.skipUnless(os.getenv('DD_INTEGRATION_TESTS'), 'Integration tests not enabled')
class Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        subprocess.check_call([DOJO_SCRIPTS / 'run_dojo.sh'])

    @classmethod
    def tearDownClass(cls):
        subprocess.check_call([DOJO_SCRIPTS / 'stop_dojo.sh'])

    def client(self, url='http://127.0.0.1:8080', user='admin', password='admin'):
        return DefectDojo(base_url=url, auth=(user, password))

    def test_login(self):
        c = self.client(password='wrong')
        with self.assertRaises(defectdojo_api_generated.exceptions.ForbiddenException):
            c.user_profile_api.user_profile_retrieve()

    def test_init(self):
        c = self.client()
        uniq = str(uuid.uuid4())
        pt = c.product_types_api.product_types_create(product_type_request=ProductTypeRequest(name=f'Test {uniq}'))
        c.products_api.products_create(
            product_request=ProductRequest(name=f'Product {uniq}', description='test', prod_type=pt.id)
        )
        # TODO: do e2e test for importing a report - just call reimport with a sample report and assert findings
