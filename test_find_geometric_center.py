import unittest
from e3_7 import GeometricCenter

class TestPoint(unittest.TestCase):

    def test_same(self):
        points = [(1,3), (2, 7), (7, 8), (9, 1)]
        k = GeometricCenter(points)
        self.assertEqual(k.find_geometric_center(), ([4.75, 4.75]))

    def test_2D(self):
        points = [(1,1), (2, 2), (3, 1)]
        k = GeometricCenter(points)
        self.assertEqual(k.find_geometric_center(), ([2, 1.333]))

        points_2 = [(1, 1), (1, 3), (3, 1), (4, 2), (4, 4)]
        k = GeometricCenter(points_2)
        self.assertEqual(k.find_geometric_center(), ([2.6, 2.2]))

    def test_3D(self):
        points = [(1,1,1), (2,2,1), (3,1,5)]
        k = GeometricCenter(points)
        self.assertEqual(k.find_geometric_center(), ([2, 1.333, 2.333]))


if __name__ == "__main__":
    unittest.main()
