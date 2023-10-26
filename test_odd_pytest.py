import pytest
from odd import is_odd

class TestClass():
	def test_prime_number(self):
		# Test if a prime number (e.g., 7) is identified as prime
         assert is_odd(7) == True

if __name__ == "__main__":
    pytest.main()