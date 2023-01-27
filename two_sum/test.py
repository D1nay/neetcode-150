from two_sum.main import twoSum
import unittest

class Test_TestTwoSum(unittest.TestCase):
    def test_1236_7(self):
        self.assertEqual(set(twoSum([1, 2, 3, 6], 7)), set([0, 3]))
    def test_33_6(self):
        self.assertEqual(set(twoSum([3, 3], 6)), set([0, 1]))
    def test_3(self):
        self.assertEqual(set(twoSum([2,7,11,15], 9)), set([0, 1]))    
    def test_324_6(self):
        self.assertEqual(set(twoSum([3, 2, 4], 6)), set([1, 2]))    
    def test_32414_8(self):
        self.assertEqual(set(twoSum([3, 2, 4, 1, 4], 8)), set([2, 4]))      

if __name__ == '__main__':
    unittest.main()
