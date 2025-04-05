# coding: utf-8

"""
Defect Dojo API v2

Defect Dojo - Open Source vulnerability Management made easy. Prefetch related parameters/responses not yet in the schema.

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

import unittest

from defectdojo_api_generated.models.note_request import NoteRequest


class TestNoteRequest(unittest.TestCase):
    """NoteRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> NoteRequest:
        """Test NoteRequest
        include_optional is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `NoteRequest`
        """
        model = NoteRequest()
        if include_optional:
            return NoteRequest(
                entry = '0',
                private = True,
                edited = True
            )
        else:
            return NoteRequest(
                entry = '0',
        )
        """

    def testNoteRequest(self):
        """Test NoteRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
