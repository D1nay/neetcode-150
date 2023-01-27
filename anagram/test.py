from anagram.main import isAnagram
import unittest

class Test_TestContainsDuplicate(unittest.TestCase):
    def test_nagaram(self):
        self.assertEqual(isAnagram("anagram", "nagaram"), True)

    def test_rat_car(self):
        self.assertEqual(isAnagram("rat", "car"), False)
if __name__ == '__main__':
    unittest.main()
