from product_of_array_except_self.main import productExceptSelf
import unittest

class Test_productExceptSelf(unittest.TestCase):
    def test_1234(self):
        nums = [1, 2, 3, 4]
        correct_output = [24, 12, 8, 6]
        self.assertEqual(productExceptSelf(nums), correct_output)
    def test_0(self):
        nums = [0]
        correct_output = [0]
        self.assertEqual(productExceptSelf(nums), correct_output)
    def test_empty(self):
        nums = []
        correct_output = [0]
        self.assertEqual(productExceptSelf(nums), correct_output)
    def test_single_integer(self):
        nums = [25]
        correct_output = [0]
        self.assertEqual(productExceptSelf(nums), correct_output)
    def test_negs(self):
        nums = [-1, 1, 0, -3, 3]
        correct_output = [0, 0, 9, 0, 0]
        self.assertEqual(productExceptSelf(nums), correct_output)        
if __name__ == '__main__':
    unittest.main()
