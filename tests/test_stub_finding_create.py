# coding: utf-8

"""
Defect Dojo API v2

Defect Dojo - Open Source vulnerability Management made easy. Prefetch related parameters/responses not yet in the schema.

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

import unittest

from defectdojo_api_generated.models.stub_finding_create import StubFindingCreate


class TestStubFindingCreate(unittest.TestCase):
    """StubFindingCreate unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> StubFindingCreate:
        """Test StubFindingCreate
        include_optional is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `StubFindingCreate`
        """
        model = StubFindingCreate()
        if include_optional:
            return StubFindingCreate(
                id = 56,
                test = 56,
                title = '',
                var_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                severity = '',
                description = '',
                reporter = 56
            )
        else:
            return StubFindingCreate(
                id = 56,
                test = 56,
                title = '',
                reporter = 56,
        )
        """

    def testStubFindingCreate(self):
        """Test StubFindingCreate"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
