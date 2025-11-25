import unittest
from square import area, perimeter


class SquareTestCase(unittest.TestCase):
    def test_area_positive(self):
        res = area(5)
        self.assertEqual(res, 25)

    def test_area_zero(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_area_one(self):
        res = area(1)
        self.assertEqual(res, 1)

    def test_area_float(self):
        res = area(2.5)
        self.assertEqual(res, 6.25)

    def test_perimeter_positive(self):
        res = perimeter(10)
        self.assertEqual(res, 40)

    def test_perimeter_zero(self):
        res = perimeter(0)
        self.assertEqual(res, 0)

    def test_perimeter_float(self):
        res = perimeter(3.5)
        self.assertEqual(res, 14.0)

    def test_area_negative(self):
        res = area(-5)
        self.assertEqual(res, 25)

    def test_perimeter_negative(self):
        res = perimeter(-10)
        self.assertEqual(res, -40)

    def test_area_large_number(self):
        res = area(1000000)
        self.assertEqual(res, 1000000000000)

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
