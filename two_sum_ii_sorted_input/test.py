from two_sum_ii_sorted_input.main import twoSum
import unittest

class Test_TestTwoSum_II(unittest.TestCase):
    def test_1(self):
        numbers = [2,7,11,15]
        target = 9
        answer = [1, 2]
        self.assertEqual(twoSum(numbers, target), answer)
    def test_2(self):
        numbers = [2,3,4]
        target = 6
        answer = [1, 3]
        self.assertEqual(twoSum(numbers, target), answer)
    def test_3(self):
        numbers = [-1, 0]
        target = -1
        answer = [1, 2]
        self.assertEqual(twoSum(numbers, target), answer)
    def test_4(self):
        numbers = [-20, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        target = -19
        answer = [1, 3]
        self.assertEqual(twoSum(numbers, target), answer)
    def test_5(self):
        numbers = [-20, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        target = 9
        answer = [2, 11]
        self.assertEqual(twoSum(numbers, target), answer)
if __name__ == '__main__':
    unittest.main()
