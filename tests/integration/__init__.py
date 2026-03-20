import os
import subprocess
import unittest
from pathlib import Path

DOJO_SCRIPTS = Path(__file__).parent.parent.parent / 'support' / 'integration'


class E2ETestCase(unittest.TestCase):
    _PARTIAL_RUN = False

    @classmethod
    def setUpClass(cls):
        if not (cls._PARTIAL_RUN or os.getenv('DD_INTEGRATION_TESTS')):
            raise unittest.SkipTest('Integration tests not enabled')
        if not cls._PARTIAL_RUN:
            subprocess.check_call([DOJO_SCRIPTS / 'run_dojo.sh'])

    @classmethod
    def tearDownClass(cls):
        if not cls._PARTIAL_RUN:
            subprocess.check_call([DOJO_SCRIPTS / 'stop_dojo.sh'])

    def skip_if_fail(self, test_dependency, *args, **kwargs):
        try:
            return test_dependency(*args, **kwargs)
        except Exception as e:
            raise unittest.SkipTest(f'dependency failed ({str(e)})')
