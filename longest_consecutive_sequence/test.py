from longest_consecutive_sequence.main import longestConsecutive
import unittest

class Test_GroupAnagrams(unittest.TestCase):
    def test_a(self):
        self.assertEqual(longestConsecutive([100,4,200,1,3,2]), 4)
    def test_b(self):
        self.assertEqual(longestConsecutive([0,3,7,2,5,8,4,6,0,1]), 9)
    def test_single_element(self):
        self.assertEqual(longestConsecutive([100]), 1)
    
if __name__ == '__main__':
    unittest.main()
