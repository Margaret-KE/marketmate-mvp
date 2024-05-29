import unittest
from app.utils import generate_random_string

class TestUtils(unittest.TestCase):
    def test_generate_random_string(self):
        # Test the generate_random_string function
        random_string = generate_random_string(length=10)
        self.assertEqual(len(random_string), 10)

if __name__ == '__main__':
    unittest.main()

