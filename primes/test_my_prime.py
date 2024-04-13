import unittest
from primes import is_prime, sum_of_primes

class TestPrimes(unittest.TestCase):

    def test_prime_low_number(self):
        self.assertFalse(is_prime(1))

    def test_prime_prime_number(self):
        self.assertTrue(is_prime(29))

    def test_prime_composite_number(self):
        self.assertFalse(is_prime(15))

    def test_sum_of_primes_empty_list(self):
        self.assertEqual(sum_of_primes([]), 0)

    def test_sum_of_primes_mixed_list(self):
        self.assertEqual(sum_of_primes([11, 15, 17, 18, 20, 100]), 28)

if __name__ == '__main__':
    unittest.main(verbosity=2)