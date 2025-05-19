#!/usr/bin/env python3

from typing import TypeVar

from defectdojo_api_generated import DefectDojo

T = TypeVar('T')


if __name__ == '__main__':
    # password publicly available in https://github.com/DefectDojo/django-DefectDojo/?tab=readme-ov-file#demo
    dojo = DefectDojo(base_url='https://demo.defectdojo.org/', auth=('admin', '1Defectdojo@demo#appsec'))
    for ind, result in enumerate(dojo.findings_api.findings_list_iterator()):
        finding = result.result
        print(f'- {ind}/{result.page.count} [{finding.severity}] {finding.title}')
