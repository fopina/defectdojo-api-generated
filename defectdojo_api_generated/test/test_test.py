# coding: utf-8

"""
    Defect Dojo API v2

    Defect Dojo - Open Source vulnerability Management made easy. Prefetch related parameters/responses not yet in the schema.

    The version of the OpenAPI document: 2.44.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from defectdojo_api_generated.models.test import Test

class TestTest(unittest.TestCase):
    """Test unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Test:
        """Test Test
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Test`
        """
        model = Test()
        if include_optional:
            return Test(
                id = 56,
                tags = [
                    ''
                    ],
                test_type_name = '',
                finding_groups = [
                    defectdojo_api_generated.models.finding_group.FindingGroup(
                        id = 56, 
                        name = '', 
                        test = 56, 
                        jira_issue = null, )
                    ],
                scan_type = '',
                title = '',
                description = '',
                target_start = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                target_end = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                estimated_time = '',
                actual_time = '',
                percent_complete = -2147483648,
                updated = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                version = '',
                build_id = '',
                commit_hash = '',
                branch_tag = '',
                engagement = 56,
                lead = 56,
                test_type = 56,
                environment = 56,
                api_scan_configuration = 56,
                notes = [
                    defectdojo_api_generated.models.note.Note(
                        id = 56, 
                        author = null, 
                        editor = null, 
                        history = [
                            defectdojo_api_generated.models.note_history.NoteHistory(
                                id = 56, 
                                current_editor = null, 
                                note_type = null, 
                                data = '', 
                                time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                            ], 
                        note_type = null, 
                        entry = '', 
                        date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        private = True, 
                        edited = True, 
                        edit_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                    ],
                files = [
                    defectdojo_api_generated.models.file.File(
                        id = 56, 
                        file = '', 
                        title = '', )
                    ]
            )
        else:
            return Test(
                id = 56,
                test_type_name = '',
                finding_groups = [
                    defectdojo_api_generated.models.finding_group.FindingGroup(
                        id = 56, 
                        name = '', 
                        test = 56, 
                        jira_issue = null, )
                    ],
                target_start = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                target_end = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                estimated_time = '',
                actual_time = '',
                updated = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                engagement = 56,
                test_type = 56,
                notes = [
                    defectdojo_api_generated.models.note.Note(
                        id = 56, 
                        author = null, 
                        editor = null, 
                        history = [
                            defectdojo_api_generated.models.note_history.NoteHistory(
                                id = 56, 
                                current_editor = null, 
                                note_type = null, 
                                data = '', 
                                time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                            ], 
                        note_type = null, 
                        entry = '', 
                        date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        private = True, 
                        edited = True, 
                        edit_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                    ],
                files = [
                    defectdojo_api_generated.models.file.File(
                        id = 56, 
                        file = '', 
                        title = '', )
                    ],
        )
        """

    def testTest(self):
        """Test Test"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
