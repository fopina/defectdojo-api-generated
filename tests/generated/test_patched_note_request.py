# coding: utf-8

"""
Defect Dojo API v2

Defect Dojo - Open Source vulnerability Management made easy. Prefetch related parameters/responses not yet in the schema.

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

import unittest

from defectdojo_api_generated.models.patched_note_request import PatchedNoteRequest


class TestPatchedNoteRequest(unittest.TestCase):
    """PatchedNoteRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PatchedNoteRequest:
        """Test PatchedNoteRequest
        include_optional is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `PatchedNoteRequest`
        """
        model = PatchedNoteRequest()
        if include_optional:
            return PatchedNoteRequest(
                entry = '0',
                private = True,
                edited = True
            )
        else:
            return PatchedNoteRequest(
        )
        """

    def testPatchedNoteRequest(self):
        """Test PatchedNoteRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
