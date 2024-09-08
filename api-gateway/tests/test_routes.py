import unittest
from unittest.mock import patch
from app import app

class TestProxyRoutes(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    @patch('requests.get')
    def test_proxy_get_success(self, mock_get):
        # Mock a successful response from an external service
        mock_get.return_value.status_code = 200
        mock_get.return_value.json = lambda: {"message": "Success"}

        response = self.app.get('/trading/5001')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"message": "Success"})

    @patch('requests.get')
    def test_proxy_get_service_not_found(self, mock_get):
        response = self.app.get('/unknown_service/some-endpoint')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json, {"message": "Service not found"})

    @patch('requests.post')
    def test_proxy_post_success(self, mock_post):
        # Mock a successful POST response
        mock_post.return_value.status_code = 200
        mock_post.return_value.json = lambda: {"message": "Post Success"}

        response = self.app.post('/wallet/5002', json={"key": "value"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"message": "Post Success"})

    @patch('requests.post')
    def test_proxy_post_service_not_found(self, mock_post):
        response = self.app.post('/unknown_service/another-endpoint', json={"key": "value"})
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json, {"message": "Service not found"})

if __name__ == '__main__':
    unittest.main()
