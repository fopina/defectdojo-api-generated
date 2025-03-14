# coding: utf-8

"""
    Defect Dojo API v2

    Defect Dojo - Open Source vulnerability Management made easy. Prefetch related parameters/responses not yet in the schema.

    The version of the OpenAPI document: 2.44.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from defectdojo_api_generated.models.finding_close_request import FindingCloseRequest

class TestFindingCloseRequest(unittest.TestCase):
    """FindingCloseRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> FindingCloseRequest:
        """Test FindingCloseRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `FindingCloseRequest`
        """
        model = FindingCloseRequest()
        if include_optional:
            return FindingCloseRequest(
                is_mitigated = True,
                mitigated = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                false_p = True,
                out_of_scope = True,
                duplicate = True
            )
        else:
            return FindingCloseRequest(
        )
        """

    def testFindingCloseRequest(self):
        """Test FindingCloseRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
