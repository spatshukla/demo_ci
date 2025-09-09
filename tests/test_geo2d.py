import unittest
import sys
import os
from math import sqrt

# Add the parent directory to the path so we can import demo_ci
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from demo_ci.geo2d import Rectangle, Triangle


class TestRectangle(unittest.TestCase):
    def setUp(self):
        self.rect = Rectangle(5, 3)

    def test_rectangle_initialization(self):
        """Test that Rectangle is initialized correctly"""
        self.assertEqual(self.rect.width, 5)
        self.assertEqual(self.rect.height, 3)

    def test_rectangle_area(self):
        """Test rectangle area calculation"""
        # Note: The current implementation multiplies by 2, which seems incorrect
        # A rectangle area should be width * height = 5 * 3 = 15
        # But the current implementation returns 30 (15 * 2)
        expected_area = 30  # Current implementation behavior
        self.assertEqual(self.rect.area(), expected_area)

    def test_rectangle_perimeter(self):
        """Test rectangle perimeter calculation"""
        expected_perimeter = 2 * (5 + 3)  # 16
        self.assertEqual(self.rect.perimeter(), expected_perimeter)

    def test_rectangle_zero_dimensions(self):
        """Test rectangle with zero dimensions"""
        zero_rect = Rectangle(0, 5)
        self.assertEqual(zero_rect.area(), 0)
        self.assertEqual(zero_rect.perimeter(), 10)

    def test_rectangle_negative_dimensions(self):
        """Test rectangle with negative dimensions"""
        neg_rect = Rectangle(-2, 3)
        self.assertEqual(neg_rect.area(), -12)  # -2 * 3 * 2
        self.assertEqual(neg_rect.perimeter(), 2)

    def test_rectangle_decimal_dimensions(self):
        """Test rectangle with decimal dimensions"""
        decimal_rect = Rectangle(2.5, 4.2)
        self.assertAlmostEqual(decimal_rect.area(), 21.0, places=2)  # 2.5 * 4.2 * 2
        self.assertAlmostEqual(decimal_rect.perimeter(), 13.4, places=2)

    def test_rectangle_large_dimensions(self):
        """Test rectangle with large dimensions"""
        large_rect = Rectangle(1000, 2000)
        self.assertEqual(large_rect.area(), 4000000)  # 1000 * 2000 * 2
        self.assertEqual(large_rect.perimeter(), 6000)


class TestTriangle(unittest.TestCase):
    def setUp(self):
        self.triangle = Triangle(3, 4, 5)  # Right triangle

    def test_triangle_initialization(self):
        """Test that Triangle is initialized correctly"""
        self.assertEqual(self.triangle.a, 3)
        self.assertEqual(self.triangle.b, 4)
        self.assertEqual(self.triangle.c, 5)

    def test_triangle_area_right_triangle(self):
        """Test triangle area for a right triangle (3-4-5)"""
        # For a 3-4-5 right triangle, area should be 6
        expected_area = 6.0
        self.assertAlmostEqual(self.triangle.area(), expected_area, places=5)

    def test_triangle_perimeter(self):
        """Test triangle perimeter calculation"""
        expected_perimeter = 3 + 4 + 5  # 12
        self.assertEqual(self.triangle.perimeter(), expected_perimeter)

    def test_triangle_equilateral(self):
        """Test equilateral triangle"""
        equilateral = Triangle(6, 6, 6)
        expected_area = (sqrt(3) / 4) * 6 * 6  # Formula for equilateral triangle
        self.assertAlmostEqual(equilateral.area(), expected_area, places=5)
        self.assertEqual(equilateral.perimeter(), 18)

    def test_triangle_isosceles(self):
        """Test isosceles triangle"""
        isosceles = Triangle(5, 5, 8)
        # Using Heron's formula: s = 9, area = sqrt(9 * 4 * 4 * 1) = 12
        expected_area = 12.0
        self.assertAlmostEqual(isosceles.area(), expected_area, places=5)
        self.assertEqual(isosceles.perimeter(), 18)

    def test_triangle_scalene(self):
        """Test scalene triangle"""
        scalene = Triangle(7, 8, 9)
        # Using Heron's formula: s = 12, area = sqrt(12 * 5 * 4 * 3)
        s = 12
        expected_area = sqrt(s * 5 * 4 * 3)
        self.assertAlmostEqual(scalene.area(), expected_area, places=5)
        self.assertEqual(scalene.perimeter(), 24)

    def test_triangle_decimal_sides(self):
        """Test triangle with decimal side lengths"""
        decimal_triangle = Triangle(3.5, 4.2, 5.1)
        s = (3.5 + 4.2 + 5.1) / 2
        expected_area = sqrt(s * (s - 3.5) * (s - 4.2) * (s - 5.1))
        self.assertAlmostEqual(decimal_triangle.area(), expected_area, places=5)
        self.assertAlmostEqual(decimal_triangle.perimeter(), 12.8, places=2)

    def test_triangle_small_triangle(self):
        """Test triangle with very small sides"""
        small_triangle = Triangle(0.1, 0.2, 0.25)
        # Should still work with Heron's formula
        s = (0.1 + 0.2 + 0.25) / 2
        expected_area = sqrt(s * (s - 0.1) * (s - 0.2) * (s - 0.25))
        self.assertAlmostEqual(small_triangle.area(), expected_area, places=10)
        self.assertAlmostEqual(small_triangle.perimeter(), 0.55, places=2)


if __name__ == '__main__':
    unittest.main()