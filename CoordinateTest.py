import unittest

from Coordinate import Coordinate


class CoordinateTest(unittest.TestCase):
    def test_itCalculatesTheDistanceFromItself(self):
        a = Coordinate(0, 0)
        self.assertEqual(0, a.distance_from(a))

    def test_itCalculatesTheDistanceFromAnotherCoordinateAlongXAxis(self):
        a = Coordinate(0, 0)
        b = Coordinate(600, 0)
        self.assertEqual(600, a.distance_from(b))

    def test_itCalculatesTheDistanceFromAnotherCoordinate(self):
        a = Coordinate(0, 0)
        b = Coordinate(300, 400)
        self.assertEqual(500, a.distance_from(b))

    # Use this code to implement Pythagoras' theorem in Coordinate.py:
    #
    # from math import hypot
    # return hypot(self.__x - other.__x, self.__y - other.__y)

if __name__ == '__main__':
    unittest.main()
