import unittest

from defectdojo_api_generated.models import AuthToken


class Test(unittest.TestCase):
    def test_all_optional(self) -> None:
        AuthToken()
