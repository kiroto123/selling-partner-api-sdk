# coding: utf-8

from __future__ import absolute_import

import unittest
import requests
import rstr

from spapi.auth.credentials import SPAPIConfig
from spapi.client import SPAPIClient
from spapi.api.customer_feedback_2024_06_01.customer_feedback_api import CustomerFeedbackApi

import spapi.models.customer_feedback_2024_06_01 as models

class TestCustomerFeedbackApi(unittest.TestCase):
    """CustomerFeedbackApi unit test stubs"""

    def setUp(self):
        # Tests Mock Server
        self.mock_server_endpoint = "http://localhost:3000"
        self.mock_server_endpoint_oauth = "http://localhost:3000/auth/o2/token"
        config = SPAPIConfig(
            client_id="clientId",
            client_secret="clientSecret",
            refresh_token="refreshToken",
            region="NA",
            scope = None
        )
        client = SPAPIClient(config, self.mock_server_endpoint_oauth, self.mock_server_endpoint)
        self.api = CustomerFeedbackApi(client.api_client)

    def tearDown(self):
        pass

    def test_get_browse_node_return_topics(self):
        browse_node_id = self._get_random_value("str", None)
        marketplace_id = self._get_random_value("str", None)
        
        self.instruct_backend_mock(self.to_camel_case("get_browse_node_return_topics"), "200")
        response = self.api.get_browse_node_return_topics_with_http_info(browse_node_id, marketplace_id, )
        self.assertEqual(200, response[1])
        self.assert_valid_response_payload(200, response[0])
        pass

    def test_get_browse_node_return_trends(self):
        browse_node_id = self._get_random_value("str", None)
        marketplace_id = self._get_random_value("str", None)
        
        self.instruct_backend_mock(self.to_camel_case("get_browse_node_return_trends"), "200")
        response = self.api.get_browse_node_return_trends_with_http_info(browse_node_id, marketplace_id, )
        self.assertEqual(200, response[1])
        self.assert_valid_response_payload(200, response[0])
        pass

    def test_get_browse_node_review_topics(self):
        browse_node_id = self._get_random_value("str", None)
        marketplace_id = self._get_random_value("str", None)
        sort_by = self._get_random_value("str", None)
        
        self.instruct_backend_mock(self.to_camel_case("get_browse_node_review_topics"), "200")
        response = self.api.get_browse_node_review_topics_with_http_info(browse_node_id, marketplace_id, sort_by, )
        self.assertEqual(200, response[1])
        self.assert_valid_response_payload(200, response[0])
        pass

    def test_get_browse_node_review_trends(self):
        browse_node_id = self._get_random_value("str", None)
        marketplace_id = self._get_random_value("str", None)
        
        self.instruct_backend_mock(self.to_camel_case("get_browse_node_review_trends"), "200")
        response = self.api.get_browse_node_review_trends_with_http_info(browse_node_id, marketplace_id, )
        self.assertEqual(200, response[1])
        self.assert_valid_response_payload(200, response[0])
        pass

    def test_get_item_browse_node(self):
        asin = self._get_random_value("str", None)
        marketplace_id = self._get_random_value("str", None)
        
        self.instruct_backend_mock(self.to_camel_case("get_item_browse_node"), "200")
        response = self.api.get_item_browse_node_with_http_info(asin, marketplace_id, )
        self.assertEqual(200, response[1])
        self.assert_valid_response_payload(200, response[0])
        pass

    def test_get_item_review_topics(self):
        asin = self._get_random_value("str", None)
        marketplace_id = self._get_random_value("str", None)
        sort_by = self._get_random_value("str", None)
        
        self.instruct_backend_mock(self.to_camel_case("get_item_review_topics"), "200")
        response = self.api.get_item_review_topics_with_http_info(asin, marketplace_id, sort_by, )
        self.assertEqual(200, response[1])
        self.assert_valid_response_payload(200, response[0])
        pass

    def test_get_item_review_trends(self):
        asin = self._get_random_value("str", None)
        marketplace_id = self._get_random_value("str", None)
        
        self.instruct_backend_mock(self.to_camel_case("get_item_review_trends"), "200")
        response = self.api.get_item_review_trends_with_http_info(asin, marketplace_id, )
        self.assertEqual(200, response[1])
        self.assert_valid_response_payload(200, response[0])
        pass


    def instruct_backend_mock(self, response: str, code: str) -> None:
        url = f"{self.mock_server_endpoint}/response/{response}/code/{code}"
        ## handle same api operation name exceptions
        if "vendor" in "api.customer_feedback_2024_06_01" and response == "getOrder":
            url += f"?qualifier=Vendor"
        if "fulfillment_inbound" in "api.customer_feedback_2024_06_01" and response == "getShipment":
            url += f"?qualifier=FbaInbound"
        if "seller_wallet" in "api.customer_feedback_2024_06_01" and response == "getAccount":
            url += f"?qualifier=SellerWallet"
        if "seller_wallet" in "api.customer_feedback_2024_06_01" and response == "getTransaction":
            url += f"?qualifier=SellerWallet"
        requests.post(url)

    def _get_random_value(self, data_type, pattern=None):
        if pattern:
            return rstr.xeger(pattern)

        basic_types = {
            'str': "test_string",
            'string': "test_string",
            'int': 123,
            'integer': 123,
            'float': 123.45,
            'bool': True,
            'boolean': True
        }

        return basic_types.get(data_type.lower(), {})

    def assert_valid_response_payload(self, status_code: int, body: any) -> None:
        if status_code != 204:
            self.assertIsNotNone(body)

    def to_camel_case(self, snake_str):
        components = snake_str.split('_')
        return components[0] + ''.join(x.title() for x in components[1:])

if __name__ == '__main__':
    unittest.main()