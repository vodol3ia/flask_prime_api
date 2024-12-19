import unittest
from app.utils import find_nth_prime

class TestUtils(unittest.TestCase):
    def test_find_nth_prime(self):
        self.assertEqual(find_nth_prime(1), 2)
        self.assertEqual(find_nth_prime(2), 3)
        self.assertEqual(find_nth_prime(3), 5)
        self.assertEqual(find_nth_prime(10), 29)

if __name__ == '__main__':
    unittest.main()
