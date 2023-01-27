import contains_duplicate
import unittest

class Test_TestContainsDuplicate(unittest.TestCase):
    def test_123(self):
        self.assertEqual(contains_duplicate.containDuplicate([1, 2, 3]), False)
    
    def test_1231(self):
        self.assertEqual(contains_duplicate.containDuplicate([1, 2, 3, 1]), True)
    def test_long1(self):
        self.assertEqual(contains_duplicate.containDuplicate([1,1,1,3,3,4,3,2,4,2]), True)

if __name__ == '__main__':
    unittest.main()
