from container_with_most_water.main import maxArea
import unittest

class Test_maxArea(unittest.TestCase):
    def test_1(self):
        height = [1,1]
        self.assertEqual(maxArea(height), 1)
    def test_2(self):
        height = [1,8,6,2,5,4,8,3,7]
        self.assertEqual(maxArea(height), 49)
    def test_3(self):
        height = [1, 2, 3, 3, 2, 1]
        self.assertEqual(maxArea(height), 6)
    def test_4(self):
        height = [1, 2, 10, 10, 2, 1]
        self.assertEqual(maxArea(height), 10)


if __name__ == '__main__':
    unittest.main()
