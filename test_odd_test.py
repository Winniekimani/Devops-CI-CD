import unittest
from odd import is_odd

class TestClass(unittest.TestCase):
	def test_prime_number(self):
		# Test if a prime number (e.g., 7) is identified as prime
         result = is_odd(7)
         self.assertTrue(result)

if __name__ == "__main__":
    unittest.main()
