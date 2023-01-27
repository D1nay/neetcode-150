import group_anagrams
import unittest

class Test_GroupAnagrams(unittest.TestCase):
    def test_a(self):
        self.assertEqual(group_anagrams.groupAnagrams(["a"]), [["a"]])

if __name__ == '__main__':
    unittest.main()
