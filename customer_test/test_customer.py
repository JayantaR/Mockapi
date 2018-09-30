import unittest
from customer import get_customer
from unittest.mock import patch


class ApiTests(unittest.TestCase):

    def test_getcustomer_returns_200(self):
        response = get_customer("0")

        # Assert that the request-response cycle completed successfully with status code 200.
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.status, "OK")


if __name__ == "__main__":
    unittest.main()