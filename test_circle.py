import unittest
import math
from circle import area, perimeter


class CircleTestCase(unittest.TestCase):
    def test_area_positive(self):
        res = area(5)
        self.assertAlmostEqual(res, 78.53981633974483)

    def test_area_zero(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_area_one(self):
        res = area(1)
        self.assertAlmostEqual(res, math.pi)

    def test_area_float(self):
        res = area(2.5)
        self.assertAlmostEqual(res, 19.634954084936208)

    def test_perimeter_positive(self):
        res = perimeter(10)
        self.assertAlmostEqual(res, 62.83185307179586)

    def test_perimeter_zero(self):
        res = perimeter(0)
        self.assertEqual(res, 0)

    def test_perimeter_one(self):
        res = perimeter(1)
        self.assertAlmostEqual(res, 2 * math.pi)

    def test_area_negative(self):
        res = area(-5)
        self.assertAlmostEqual(res, 78.53981633974483)

    def test_perimeter_negative(self):
        res = perimeter(-10)
        self.assertAlmostEqual(res, -62.83185307179586)

    def test_area_large_number(self):
        res = area(1000000)
        self.assertAlmostEqual(res, math.pi * 1000000 ** 2)

    def test_area_invalid_type_string(self):
        with self.assertRaises(TypeError):
            area("abc")

    def test_area_invalid_type_none(self):
        with self.assertRaises(TypeError):
            area(None)

    def test_area_invalid_type_list(self):
        with self.assertRaises(TypeError):
            area([1, 2, 3])


if __name__ == '__main__':
    unittest.main()
