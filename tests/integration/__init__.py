import os
import subprocess
import unittest
from pathlib import Path

DOJO_SCRIPTS = Path(__file__).parent.parent.parent / 'support' / 'integration'
_DOJO_REFCOUNT = 0


class E2ETestCase(unittest.TestCase):
    _PARTIAL_RUN = False

    @classmethod
    def setUpClass(cls):
        global _DOJO_REFCOUNT
        if not (cls._PARTIAL_RUN or os.getenv('DD_INTEGRATION_TESTS')):
            raise unittest.SkipTest('Integration tests not enabled')
        if not cls._PARTIAL_RUN:
            if _DOJO_REFCOUNT == 0:
                subprocess.check_call([DOJO_SCRIPTS / 'run_dojo.sh'])
            _DOJO_REFCOUNT += 1

    @classmethod
    def tearDownClass(cls):
        global _DOJO_REFCOUNT
        if not cls._PARTIAL_RUN:
            _DOJO_REFCOUNT -= 1
            if _DOJO_REFCOUNT == 0:
                subprocess.check_call([DOJO_SCRIPTS / 'stop_dojo.sh'])

    def skip_if_fail(self, test_dependency, *args, **kwargs):
        try:
            return test_dependency(*args, **kwargs)
        except Exception as e:
            raise unittest.SkipTest(f'dependency failed ({str(e)})')
