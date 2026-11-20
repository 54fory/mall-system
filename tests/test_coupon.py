import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from coupon import calculate_price


class TestCoupon(unittest.TestCase):

    def test_normal_discount(self):
        self.assertEqual(calculate_price(100, 0.20), 80.0)

    def test_default_discount(self):
        self.assertEqual(calculate_price(100), 80.0)

    def test_zero_discount(self):
        self.assertEqual(calculate_price(100, 0), 100.0)

    def test_full_discount(self):
        self.assertEqual(calculate_price(100, 1), 0.0)

    def test_negative_price(self):
        with self.assertRaises(ValueError):
            calculate_price(-100)

    def test_invalid_discount(self):
        with self.assertRaises(ValueError):
            calculate_price(100, 1.5)

        with self.assertRaises(ValueError):
            calculate_price(100, -0.1)


if __name__ == "__main__":
    unittest.main()
