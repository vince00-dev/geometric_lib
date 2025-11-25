import unittest
from rectangle import area, perimeter


class RectangleTestCase(unittest.TestCase):
    def test_zero_mul(self):
        res = area(10, 0)
        self.assertEqual(res, 0)

    def test_square_mul(self):
        res = area(10, 10)
        self.assertEqual(res, 100)

    def test_area_positive(self):
        res = area(5, 3)
        self.assertEqual(res, 15)

    def test_area_float(self):
        res = area(2.5, 4.0)
        self.assertEqual(res, 10.0)

    def test_perimeter_basic(self):
        res = perimeter(10, 5)
        self.assertEqual(res, 30)

    def test_perimeter_zero(self):
        res = perimeter(0, 0)
        self.assertEqual(res, 0)

    def test_perimeter_float(self):
        res = perimeter(3.5, 2.5)
        self.assertEqual(res, 12.0)

    def test_area_negative(self):
        res = area(-5, -3)
        self.assertEqual(res, 15)

    def test_area_mixed_signs(self):
        res = area(-5, 3)
        self.assertEqual(res, -15)

    def test_perimeter_negative(self):
        res = perimeter(-10, -5)
        self.assertEqual(res, -30)

    def test_area_large_numbers(self):
        """Test with very large dimensions"""
        res = area(1000000, 1000000)
        self.assertEqual(res, 1000000000000)

    def test_area_invalid_type_string(self):
        res = area("abc", 5)
        self.assertEqual(res, "abcabcabcabcabc")

    def test_area_invalid_type_none(self):
        with self.assertRaises(TypeError):
            area(None, 10)

    def test_area_invalid_type_list(self):
        res = area([1, 2], 5)
        self.assertEqual(res, [1, 2, 1, 2, 1, 2, 1, 2, 1, 2])


if __name__ == '__main__':
    unittest.main()
