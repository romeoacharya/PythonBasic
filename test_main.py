import unittest
from unittest.mock import patch

import main


class MainTests(unittest.TestCase):
    def test_calculate_average(self):
        self.assertEqual(main.calculate_average(), 0)
        self.assertEqual(main.calculate_average(10, 20, 30), 20)

    def test_binary_search(self):
        values = [10, 20, 30, 40, 50]
        self.assertEqual(main.binary_search(values, 30), 2)
        self.assertEqual(main.binary_search(values, 60), -1)

    def test_is_palindrome(self):
        self.assertTrue(main.is_palindrome("Never odd or even"))
        self.assertFalse(main.is_palindrome("hello"))

    def test_factorial(self):
        self.assertEqual(main.factorial(0), 1)
        self.assertEqual(main.factorial(5), 120)
        with self.assertRaises(ValueError):
            main.factorial(-1)

    def test_fibonacci(self):
        self.assertEqual(main.fibonacci(0), 0)
        self.assertEqual(main.fibonacci(1), 1)
        self.assertEqual(main.fibonacci(10), 55)
        with self.assertRaises(ValueError):
            main.fibonacci(-1)

    def test_gcd_and_lcm(self):
        self.assertEqual(main.gcd(48, 18), 6)
        self.assertEqual(main.gcd(-48, 18), 6)
        self.assertEqual(main.lcm(12, 18), 36)
        self.assertEqual(main.lcm(0, 18), 0)

    def test_is_prime(self):
        self.assertTrue(main.is_prime(29))
        self.assertFalse(main.is_prime(1))
        self.assertFalse(main.is_prime(30))

    def test_prime_factors(self):
        self.assertEqual(main.prime_factors(84), [2, 2, 3, 7])
        self.assertEqual(main.prime_factors(13), [13])

    def test_number_conversions(self):
        self.assertEqual(main.decimal_to_binary(10), "1010")
        self.assertEqual(main.binary_to_decimal("1010"), 10)
        self.assertEqual(main.decimal_to_hexadecimal(255), "ff")
        self.assertEqual(main.hexadecimal_to_decimal("ff"), 255)
        with self.assertRaises(ValueError):
            main.decimal_to_binary(-1)
        with self.assertRaises(ValueError):
            main.decimal_to_hexadecimal(-1)

    def test_roll_two_dice(self):
        with patch("random.randint", side_effect=[1, 6]):
            self.assertEqual(main.roll_two_dice(), (1, 6))

    def test_get_all_subset_of_string(self):
        subsets = main.get_all_subset_of_string("ab")
        self.assertCountEqual(subsets, ["", "a", "b", "ab"])
        self.assertEqual(main.get_all_subset_of_string(""), [""])

    def test_set_operations(self):
        seta = {23, 45, 34}
        setb = {23, 45, 34, 56, 78}

        self.assertEqual(seta.union(setb), {23, 45, 34, 56, 78})
        self.assertEqual(seta.intersection(setb), {23, 45, 34})
        self.assertEqual(setb.difference(seta), {56, 78})
        self.assertEqual(seta.symmetric_difference(setb), {56, 78})

print("All tests passed successfully!")

if __name__ == "__main__":
    unittest.main()