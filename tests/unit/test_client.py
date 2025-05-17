import unittest

from defectdojo_api_generated import Configuration, DefectDojo


class Test(unittest.TestCase):
    def test_init(self) -> None:
        c = DefectDojo(base_url='https://demo.defectdojo.org/', auth=('a', 'p'))
        self.assertEqual(c.config.host, 'https://demo.defectdojo.org/')
        self.assertEqual(c.config.username, 'a')
        self.assertEqual(c.config.password, 'p')

        c = DefectDojo(base_url='https://ignore.me', config=Configuration(host='https://demo.defectdojo.org/'))
        self.assertEqual(c.config.host, 'https://demo.defectdojo.org/')
