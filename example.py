#!/usr/bin/env python3

from defectdojo_api_generated.client import DefectDojo

if __name__ == '__main__':
    # password publicly available in https://github.com/DefectDojo/django-DefectDojo/?tab=readme-ov-file#demo
    # dojo = DefectDojo('https://demo.defectdojo.org/', os.environ['DOJO_TOKEN'])
    dojo = DefectDojo('https://demo.defectdojo.org', auth=('admin', '1Defectdojo@demo#appsec'))
    r = dojo.findings_api.findings_list()
    print(r.json())
