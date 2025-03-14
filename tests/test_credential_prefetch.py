# coding: utf-8

"""
Defect Dojo API v2

Defect Dojo - Open Source vulnerability Management made easy. Prefetch related parameters/responses not yet in the schema.

The version of the OpenAPI document: 2.44.1
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

import unittest

from defectdojo_api_generated.models.credential_prefetch import CredentialPrefetch


class TestCredentialPrefetch(unittest.TestCase):
    """CredentialPrefetch unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CredentialPrefetch:
        """Test CredentialPrefetch
        include_optional is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `CredentialPrefetch`
        """
        model = CredentialPrefetch()
        if include_optional:
            return CredentialPrefetch(
                environment = {
                    'key' : defectdojo_api_generated.models.finding_environment.FindingEnvironment(
                        id = 56, 
                        name = '', )
                    },
                notes = {
                    'key' : defectdojo_api_generated.models.note.Note(
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
                    }
            )
        else:
            return CredentialPrefetch(
        )
        """

    def testCredentialPrefetch(self):
        """Test CredentialPrefetch"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
