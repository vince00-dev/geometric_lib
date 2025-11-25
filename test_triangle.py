import unittest
from triangle import area, perimeter


class TriangleTestCase(unittest.TestCase):
    def test_area_positive(self):
        res = area(10, 5)
        self.assertEqual(res, 25.0)

    def test_area_zero_base(self):
        res = area(0, 10)
        self.assertEqual(res, 0)

    def test_area_zero_height(self):
        res = area(10, 0)
        self.assertEqual(res, 0)

    def test_area_float(self):
        res = area(6.5, 4.0)
        self.assertEqual(res, 13.0)

    def test_perimeter_positive(self):
        res = perimeter(3, 4, 5)
        self.assertEqual(res, 12)

    def test_perimeter_equal_sides(self):
        res = perimeter(5, 5, 5)
        self.assertEqual(res, 15)

    def test_perimeter_float(self):
        res = perimeter(2.5, 3.5, 4.0)
        self.assertEqual(res, 10.0)

    def test_area_negative_base(self):
        """Test that negative base returns negative area"""
        res = area(-10, 5)
        self.assertEqual(res, -25.0)

    def test_area_negative_height(self):
        """Test that negative height returns negative area"""
        res = area(10, -5)
        self.assertEqual(res, -25.0)

    def test_perimeter_negative_sides(self):
        """Test perimeter with negative sides"""
        res = perimeter(-3, -4, -5)
        self.assertEqual(res, -12)

    def test_area_large_numbers(self):
        """Test with very large base and height"""
        res = area(1000000, 1000000)
        self.assertEqual(res, 500000000000.0)

    def test_perimeter_invalid_triangle(self):
        res = perimeter(1, 2, 10)
        self.assertEqual(res, 13)

    def test_perimeter_degenerate_triangle(self):
        res = perimeter(3, 4, 7)
        self.assertEqual(res, 14)

    def test_area_invalid_type_string(self):
        with self.assertRaises(TypeError):
            area("abc", 5)

    def test_area_invalid_type_none(self):
        with self.assertRaises(TypeError):
            area(None, 10)

    def test_area_invalid_type_list(self):
        with self.assertRaises(TypeError):
            area([1, 2], 5)


if __name__ == '__main__':
    unittest.main()
