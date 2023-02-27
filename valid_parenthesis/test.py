from valid_parenthesis.main import isValid
import unittest

class Test_validPar(unittest.TestCase):
    def test_1(self):
        s = "()"
        self.assertEqual(isValid(s), True)
    def test_2(self):
        s = "()[]{}"
        self.assertEqual(isValid(s), True)
    def test_3(self):
        s = "(]"
        self.assertEqual(isValid(s), False)
    def test_4(self):
        s = "((((((])))))"
        self.assertEqual(isValid(s), False)
    

if __name__ == '__main__':
    unittest.main()
