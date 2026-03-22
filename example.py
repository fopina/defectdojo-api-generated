#!/usr/bin/env python3

PASSWORD = '1Defectdojo@demo#appsec'


def main():
    # README +++
    from defectdojo_api_generated import DefectDojo

    # password publicly available in https://github.com/DefectDojo/django-DefectDojo/?tab=readme-ov-file#demo
    dojo = DefectDojo(base_url='https://demo.defectdojo.org/', auth=('admin', PASSWORD))
    for ind, finding in enumerate(dojo.findings_api.list_iterator(title='Stored XSS')):
        if not ind:
            print(f'Total matched findings: {finding.page.count}')
        print(f'- [{finding.result.severity}] {finding.result.title} - {finding.result.description}')
    r = dojo.system_settings_api.list(limit=1)
    print(f'- {r.results[0]}')
    # README ---


if __name__ == '__main__':
    main()
