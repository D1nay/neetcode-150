from group_anagrams.main import groupAnagrams
import unittest

class Test_GroupAnagrams(unittest.TestCase):
    def test_a(self):
        self.assertEqual(groupAnagrams(["a"]), [["a"]])

if __name__ == '__main__':
    unittest.main()
