import valid_anagram
import unittest

class Test_TestContainsDuplicate(unittest.TestCase):
    def test_nagaram(self):
        self.assertEqual(valid_anagram.isAnagram("anagram", "nagaram"), True)

    def test_rat_car(self):
        self.assertEqual(valid_anagram.isAnagram("rat", "car"), False)
if __name__ == '__main__':
    unittest.main()
