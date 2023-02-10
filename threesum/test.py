from threesum.main import threeSum
import unittest

class Test_3sum(unittest.TestCase):
    def test_1(self):
        nums = [-1,0,1,2,-1,-4]
        output = [[-1,-1,2],[-1,0,1]]
        self.assertEqual(threeSum(nums), output)
    def test_no_solution(self):
        nums = [0,1,1]
        output = []
        self.assertEqual(threeSum(nums), output)
    def test_000(self):
        nums = [0, 0, 0]
        output = [[0,0,0]]
        self.assertEqual(threeSum(nums), output)
if __name__ == '__main__':
    unittest.main()
