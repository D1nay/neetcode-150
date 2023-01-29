from top_k_frequent_elements.main import topKFrequent
import unittest

class Test_TestTopKFrequent(unittest.TestCase):
    def test_123(self):
        nums = [1,1,1,2,2,3]
        k = 2
        correct_output = [1, 2]
        self.assertEqual(set(topKFrequent(nums, k)), set(correct_output)) 

    def test_1(self):
        nums = [1]
        k = 1
        correct_output = [1]
        self.assertEqual(set(topKFrequent(nums, k)), set(correct_output)) 
 
    # def test_10_20_30(self):
    #     nums = [1, 2, 2, 3, 3, 3, 4, 4]
    #     k = 2
    #     correct_output = [3, 2]
    #     self.assertEqual(set(topKFrequent(nums, k)), set(correct_output)) 

if __name__ == '__main__':
    unittest.main()
