# coding: utf-8

"""
Defect Dojo API v2

Defect Dojo - Open Source vulnerability Management made easy. Prefetch related parameters/responses not yet in the schema.

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

import unittest

from defectdojo_api_generated.models.paginated_engagement_list import PaginatedEngagementList


class TestPaginatedEngagementList(unittest.TestCase):
    """PaginatedEngagementList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PaginatedEngagementList:
        """Test PaginatedEngagementList
        include_optional is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `PaginatedEngagementList`
        """
        model = PaginatedEngagementList()
        if include_optional:
            return PaginatedEngagementList(
                count = 123,
                next = 'http://api.example.org/accounts/?offset=400&limit=100',
                previous = 'http://api.example.org/accounts/?offset=200&limit=100',
                results = [
                    defectdojo_api_generated.models.engagement.Engagement(
                        id = 56, 
                        tags = [
                            ''
                            ], 
                        name = '', 
                        description = '', 
                        version = '', 
                        first_contacted = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                        target_start = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                        target_end = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                        reason = '', 
                        updated = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        active = True, 
                        tracker = '', 
                        test_strategy = '', 
                        threat_model = True, 
                        api_test = True, 
                        pen_test = True, 
                        check_list = True, 
                        status = 'Not Started', 
                        progress = '', 
                        tmodel_path = '', 
                        done_testing = True, 
                        engagement_type = 'Interactive', 
                        build_id = '', 
                        commit_hash = '', 
                        branch_tag = '', 
                        source_code_management_uri = '', 
                        deduplication_on_engagement = True, 
                        lead = 56, 
                        requester = 56, 
                        preset = 56, 
                        report_type = 56, 
                        product = 56, 
                        build_server = 56, 
                        source_code_management_server = 56, 
                        orchestration_engine = 56, 
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
                        risk_acceptance = [
                            56
                            ], )
                    ]
            )
        else:
            return PaginatedEngagementList(
                count = 123,
                results = [
                    defectdojo_api_generated.models.engagement.Engagement(
                        id = 56, 
                        tags = [
                            ''
                            ], 
                        name = '', 
                        description = '', 
                        version = '', 
                        first_contacted = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                        target_start = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                        target_end = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                        reason = '', 
                        updated = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        active = True, 
                        tracker = '', 
                        test_strategy = '', 
                        threat_model = True, 
                        api_test = True, 
                        pen_test = True, 
                        check_list = True, 
                        status = 'Not Started', 
                        progress = '', 
                        tmodel_path = '', 
                        done_testing = True, 
                        engagement_type = 'Interactive', 
                        build_id = '', 
                        commit_hash = '', 
                        branch_tag = '', 
                        source_code_management_uri = '', 
                        deduplication_on_engagement = True, 
                        lead = 56, 
                        requester = 56, 
                        preset = 56, 
                        report_type = 56, 
                        product = 56, 
                        build_server = 56, 
                        source_code_management_server = 56, 
                        orchestration_engine = 56, 
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
                        risk_acceptance = [
                            56
                            ], )
                    ],
        )
        """

    def testPaginatedEngagementList(self):
        """Test PaginatedEngagementList"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
