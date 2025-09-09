import unittest
import sys
import os
from math import sqrt, pi

# Add the parent directory to the path so we can import demo_ci
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from demo_ci.geo3d import Cuboid, Pyramid, Sphere, Cylinder


class TestCuboid(unittest.TestCase):
    def setUp(self):
        self.cuboid = Cuboid(3, 4, 5)

    def test_cuboid_initialization(self):
        """Test that Cuboid is initialized correctly"""
        self.assertEqual(self.cuboid.width, 3)
        self.assertEqual(self.cuboid.height, 4)
        self.assertEqual(self.cuboid.depth, 5)

    def test_cuboid_volume(self):
        """Test cuboid volume calculation"""
        expected_volume = 3 * 4 * 5  # 60
        self.assertEqual(self.cuboid.volume(), expected_volume)

    def test_cuboid_surface_area(self):
        """Test cuboid surface area calculation"""
        # Surface area = 2(wh + wd + hd) = 2(12 + 15 + 20) = 94
        expected_surface_area = 2 * (3*4 + 3*5 + 4*5)  # 94
        self.assertEqual(self.cuboid.surface_area(), expected_surface_area)

    def test_cuboid_cube(self):
        """Test cuboid when it's actually a cube"""
        cube = Cuboid(4, 4, 4)
        self.assertEqual(cube.volume(), 64)
        self.assertEqual(cube.surface_area(), 96)  # 6 * 4^2

    def test_cuboid_zero_dimensions(self):
        """Test cuboid with zero dimensions"""
        zero_cuboid = Cuboid(0, 4, 5)
        self.assertEqual(zero_cuboid.volume(), 0)
        self.assertEqual(zero_cuboid.surface_area(), 40)  # 2 * (0 + 0 + 20)

    def test_cuboid_decimal_dimensions(self):
        """Test cuboid with decimal dimensions"""
        decimal_cuboid = Cuboid(2.5, 3.2, 4.1)
        expected_volume = 2.5 * 3.2 * 4.1
        expected_surface_area = 2 * (2.5*3.2 + 2.5*4.1 + 3.2*4.1)
        self.assertAlmostEqual(decimal_cuboid.volume(), expected_volume, places=5)
        self.assertAlmostEqual(decimal_cuboid.surface_area(), expected_surface_area, places=5)


class TestPyramid(unittest.TestCase):
    def setUp(self):
        self.pyramid = Pyramid(6, 8, 10)

    def test_pyramid_initialization(self):
        """Test that Pyramid is initialized correctly"""
        self.assertEqual(self.pyramid.base_width, 6)
        self.assertEqual(self.pyramid.base_depth, 8)
        self.assertEqual(self.pyramid.height, 10)

    def test_pyramid_volume(self):
        """Test pyramid volume calculation"""
        # Volume = (1/3) * base_area * height = (1/3) * 6 * 8 * 10 = 160
        expected_volume = (1/3) * 6 * 8 * 10
        self.assertAlmostEqual(self.pyramid.volume(), expected_volume, places=5)

    def test_pyramid_surface_area(self):
        """Test pyramid surface area calculation"""
        # This test validates the current implementation
        slant_height = sqrt((6/2)**2 + 10**2)  # sqrt(9 + 100) = sqrt(109)
        base_area = 6 * 8  # 48
        lateral_area = 2 * (6 * slant_height + 8 * slant_height)
        expected_surface_area = base_area + lateral_area
        self.assertAlmostEqual(self.pyramid.surface_area(), expected_surface_area, places=5)

    def test_pyramid_square_base(self):
        """Test pyramid with square base"""
        square_pyramid = Pyramid(5, 5, 12)
        expected_volume = (1/3) * 5 * 5 * 12  # 100
        self.assertAlmostEqual(square_pyramid.volume(), expected_volume, places=5)

    def test_pyramid_zero_height(self):
        """Test pyramid with zero height"""
        flat_pyramid = Pyramid(4, 6, 0)
        self.assertEqual(flat_pyramid.volume(), 0)
        # Surface area should just be the base area when height is 0
        self.assertEqual(flat_pyramid.surface_area(), 24)  # 4 * 6

    def test_pyramid_decimal_dimensions(self):
        """Test pyramid with decimal dimensions"""
        decimal_pyramid = Pyramid(3.5, 4.2, 7.8)
        expected_volume = (1/3) * 3.5 * 4.2 * 7.8
        self.assertAlmostEqual(decimal_pyramid.volume(), expected_volume, places=5)


class TestSphere(unittest.TestCase):
    def setUp(self):
        self.sphere = Sphere(7)

    def test_sphere_initialization(self):
        """Test that Sphere is initialized correctly"""
        self.assertEqual(self.sphere.radius, 7)

    def test_sphere_volume(self):
        """Test sphere volume calculation"""
        # Volume = (4/3) * π * r^3
        # Note: The implementation uses 3.14159 instead of math.pi
        expected_volume = (4/3) * 3.14159 * (7**3)
        self.assertAlmostEqual(self.sphere.volume(), expected_volume, places=2)

    def test_sphere_surface_area(self):
        """Test sphere surface area calculation"""
        # Surface area = 4 * π * r^2
        expected_surface_area = 4 * 3.14159 * (7**2)
        self.assertAlmostEqual(self.sphere.surface_area(), expected_surface_area, places=2)

    def test_sphere_unit_radius(self):
        """Test sphere with unit radius"""
        unit_sphere = Sphere(1)
        expected_volume = (4/3) * 3.14159
        expected_surface_area = 4 * 3.14159
        self.assertAlmostEqual(unit_sphere.volume(), expected_volume, places=5)
        self.assertAlmostEqual(unit_sphere.surface_area(), expected_surface_area, places=5)

    def test_sphere_zero_radius(self):
        """Test sphere with zero radius"""
        point_sphere = Sphere(0)
        self.assertEqual(point_sphere.volume(), 0)
        self.assertEqual(point_sphere.surface_area(), 0)

    def test_sphere_decimal_radius(self):
        """Test sphere with decimal radius"""
        decimal_sphere = Sphere(2.5)
        expected_volume = (4/3) * 3.14159 * (2.5**3)
        expected_surface_area = 4 * 3.14159 * (2.5**2)
        self.assertAlmostEqual(decimal_sphere.volume(), expected_volume, places=5)
        self.assertAlmostEqual(decimal_sphere.surface_area(), expected_surface_area, places=5)


class TestCylinder(unittest.TestCase):
    def setUp(self):
        self.cylinder = Cylinder(5, 12)

    def test_cylinder_initialization(self):
        """Test that Cylinder is initialized correctly"""
        self.assertEqual(self.cylinder.radius, 5)
        self.assertEqual(self.cylinder.height, 12)

    def test_cylinder_volume(self):
        """Test cylinder volume calculation"""
        # Volume = π * r^2 * h
        expected_volume = 3.14159 * (5**2) * 12
        self.assertAlmostEqual(self.cylinder.volume(), expected_volume, places=2)

    def test_cylinder_surface_area(self):
        """Test cylinder surface area calculation"""
        # Surface area = 2 * π * r * (r + h)
        expected_surface_area = 2 * 3.14159 * 5 * (5 + 12)
        self.assertAlmostEqual(self.cylinder.surface_area(), expected_surface_area, places=2)

    def test_cylinder_unit_radius_height(self):
        """Test cylinder with unit radius and height"""
        unit_cylinder = Cylinder(1, 1)
        expected_volume = 3.14159
        expected_surface_area = 2 * 3.14159 * 1 * 2  # 2 * π * 1 * (1 + 1)
        self.assertAlmostEqual(unit_cylinder.volume(), expected_volume, places=5)
        self.assertAlmostEqual(unit_cylinder.surface_area(), expected_surface_area, places=5)

    def test_cylinder_zero_height(self):
        """Test cylinder with zero height (essentially a circle)"""
        flat_cylinder = Cylinder(3, 0)
        self.assertEqual(flat_cylinder.volume(), 0)
        expected_surface_area = 2 * 3.14159 * 3 * 3  # Only the top and bottom circles
        self.assertAlmostEqual(flat_cylinder.surface_area(), expected_surface_area, places=5)

    def test_cylinder_zero_radius(self):
        """Test cylinder with zero radius"""
        line_cylinder = Cylinder(0, 5)
        self.assertEqual(line_cylinder.volume(), 0)
        self.assertEqual(line_cylinder.surface_area(), 0)

    def test_cylinder_decimal_dimensions(self):
        """Test cylinder with decimal dimensions"""
        decimal_cylinder = Cylinder(2.8, 6.3)
        expected_volume = 3.14159 * (2.8**2) * 6.3
        expected_surface_area = 2 * 3.14159 * 2.8 * (2.8 + 6.3)
        self.assertAlmostEqual(decimal_cylinder.volume(), expected_volume, places=5)
        self.assertAlmostEqual(decimal_cylinder.surface_area(), expected_surface_area, places=5)


if __name__ == '__main__':
    unittest.main()