import unittest
from app import create_app

class TestAPI(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

    def test_valid_prime(self):
        response = self.client.get('/prime/10')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"n": 10, "nth_prime": 29})

    def test_negative_input(self):
        response = self.client.get('/prime/-5')
        self.assertEqual(response.status_code, 400)
        self.assertIn("n must be greater than or equal to 1", response.json['error'])

    def test_non_numeric_input(self):
        response = self.client.get('/prime/abc')
        self.assertEqual(response.status_code, 400)
        self.assertIn("Invalid input", response.json['error'])

    def test_empty_input(self):
        response = self.client.get('/prime/')
        self.assertEqual(response.status_code, 404)  # No route

    def test_large_input(self):
        response = self.client.get('/prime/10000')  # Very large number
        self.assertEqual(response.status_code, 200)  
