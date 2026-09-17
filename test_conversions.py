import unittest
import warnings

from dec2base import dec2base
from fracbase2dex import fracbase2dex
from fracdex2base import fracdex2base
from fracbase2base import fracbase2base


class TestDec2Base(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(dec2base(0, 10), '0')
        self.assertEqual(dec2base(10, 2), '1010')
        self.assertEqual(dec2base(255, 16), 'FF')

    def test_errors(self):
        for args in [(-1, 10), (10, 1), (10, 37), (10, 2.5), (True, 2)]:
            with self.assertRaises(ValueError):
                dec2base(*args)


class TestFracBase2Dex(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(fracbase2dex('FF', 16), 255)
        self.assertEqual(fracbase2dex('1010', 2), 10)
        self.assertAlmostEqual(fracbase2dex('0.5', 10), 0.5)
        self.assertAlmostEqual(fracbase2dex('.1', 2), 0.5)

    def test_errors(self):
        with self.assertRaises(ValueError):
            fracbase2dex(123, 10)
        with self.assertRaises(ValueError):
            fracbase2dex('1G', 16)
        with self.assertRaises(ValueError):
            fracbase2dex('1.2.3', 10)
        with self.assertRaises(ValueError):
            fracbase2dex('10', 1)


class TestFracDex2Base(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(fracdex2base(255, 16), 'FF')
        self.assertEqual(fracdex2base(10, 2), '1010')
        self.assertEqual(fracdex2base(0.5, 2), '0.1')
        self.assertEqual(fracdex2base(0, 36), '0')

    def test_truncation_warning(self):
        with warnings.catch_warnings(record=True) as caught:
            warnings.simplefilter('always')
            result = fracdex2base(0.1, 2)
        self.assertEqual(result, '0.0001100110')
        self.assertTrue(any('truncated' in str(w.message) for w in caught))

    def test_errors(self):
        for args in [(-1, 10), ('abc', 10), (True, 10), (10, 37)]:
            with self.assertRaises(ValueError):
                fracdex2base(*args)


class TestFracBase2Base(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(fracbase2base('FF', 16, 2), '11111111')
        self.assertEqual(fracbase2base('1010', 2, 10), '10')
        self.assertEqual(fracbase2base('0.5', 10, 2), '0.1')
        self.assertEqual(fracbase2base('Z', 36, 10), '35')

    def test_errors(self):
        with self.assertRaises(ValueError):
            fracbase2base(123, 10, 2)
        with self.assertRaises(ValueError):
            fracbase2base('1G', 16, 2)


if __name__ == '__main__':
    unittest.main()
