from min_stack.main import MinStack
import unittest

class Test_minStack(unittest.TestCase):
    def test_1(self):
        ms = MinStack()
        ms.push(-2)
        ms.push(0)
        ms.push(-3)
        self.assertEqual(ms.getMin(), -3)
        ms.pop()
        self.assertEqual(ms.top(), 0)
        self.assertEqual(ms.getMin(), -2)

if __name__ == '__main__':
    unittest.main()
