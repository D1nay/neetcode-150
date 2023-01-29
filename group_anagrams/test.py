from group_anagrams.main import groupAnagrams
import unittest

class Test_GroupAnagrams(unittest.TestCase):
    def test_a(self):
        self.assertEqual(groupAnagrams(["a"]), [["a"]])
    def test_two_word(self):
        self.assertEqual(groupAnagrams(["eat", "gotta"]), [["eat"], ["gotta"]])
    def test_empty(self):
        self.assertEqual(groupAnagrams([""]), [[""]])
    def test_eat(self):
        words = ["eat","tea","tan","ate","nat","bat"]
        set_function = {frozenset(item) for item in groupAnagrams(words)}
        set_true = {frozenset(["bat"]), frozenset(["nat","tan"]), frozenset(["ate","eat","tea"])}
        self.assertEqual(set_function, set_true)
    

if __name__ == '__main__':
    unittest.main()
