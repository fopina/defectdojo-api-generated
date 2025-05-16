#!/usr/bin/env python3

from defectdojo_api_generated import Configuration, DefectDojo

if __name__ == '__main__':
    # password publicly available in https://github.com/DefectDojo/django-DefectDojo/?tab=readme-ov-file#demo
    dojo = DefectDojo(base_url='https://demo.defectdojo.org/', auth=('admin', '1Defectdojo@demo#appsec'))
    r = dojo.findings_api.findings_list(limit=1)
    print(f'{r.count} findings, example:')
    print(f'- [{r.results[0].severity}] {r.results[0].title} - {r.results[0].description}')

    dojo = DefectDojo(
        config=Configuration(host='https://demo.defectdojo.org', username='admin', password='1Defectdojo@demo#appsec')
    )
    r = dojo.system_settings_api.system_settings_list(limit=1)
    print(f'{r.count} settings')
    print(f'- {r.results[0]}')
