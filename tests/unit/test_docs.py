import re
import unittest
from pathlib import Path


class Test(unittest.TestCase):
    def test_asciinema(self) -> None:
        """make sure the same asciinema link is used in both README and CLI docs"""
        link_re = re.compile(r'asciinema.org/a/(.*?)\.')
        d = Path(__file__).parent.parent.parent
        links = link_re.findall((d / 'README.md').read_text())
        links_docs = link_re.findall((d / 'docs' / 'cli.md').read_text())
        self.assertEqual(len(links), 1)
        self.assertEqual(links, links_docs)
