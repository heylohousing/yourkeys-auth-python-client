"""
    Yourkeys Public API

    This API exposes endpoints that can be used to interact with the Yourkeys system  # noqa: E501

    The version of the OpenAPI document: v1
    Contact: support@yourkeys.com
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import openapi_client
from openapi_client.model.client_party import ClientParty
globals()['ClientParty'] = ClientParty
from openapi_client.model.client import Client


class TestClient(unittest.TestCase):
    """Client unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testClient(self):
        """Test Client"""
        # FIXME: construct object with mandatory attributes with example values
        # model = Client()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
