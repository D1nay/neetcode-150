from reverse_polish.main import Solution
import unittest

class Test_reversePolish(unittest.TestCase):
    def test_1(self):
        tokens = ["2","1","+","3","*"]
        self.assertEqual(Solution.evalRPN(self, tokens), 9)
    def test_2(self):
        tokens = ["4","13","5","/","+"]
        self.assertEqual(Solution.evalRPN(self, tokens), 6)
    def test_3(self):
        tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
        self.assertEqual(Solution.evalRPN(self, tokens), 22)



if __name__ == '__main__':
    unittest.main()
