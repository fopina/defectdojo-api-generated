#!/usr/bin/env python3

import os

from defectdojo_api_generated.client import DefectDojo


if __name__ == '__main__':
    dojo = DefectDojo('https://demo.defectdojo.org/', os.environ['DOJO_TOKEN'])
    r = dojo.findings_api.findings_list()
    print(r.json())
