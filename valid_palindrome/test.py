from valid_palindrome.main import isPalindrome
import unittest

class Test_TestTwoSum(unittest.TestCase):
    def test_1(self):
        input = "A man, a plan, a canal: Panama"
        output = True
        self.assertEqual(isPalindrome(input), output)
    def test_2(self):
        input = "race a car"
        output = False
        self.assertEqual(isPalindrome(input), output)
    def test_1_space(self):
        input = " "
        output = True
        self.assertEqual(isPalindrome(input), output)
if __name__ == '__main__':
    unittest.main()
