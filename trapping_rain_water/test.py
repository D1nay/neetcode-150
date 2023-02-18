from trapping_rain_water.main import trap
import unittest

class Test_trappingWater(unittest.TestCase):
    def test_1(self):
        height = [0,1,0,2,1,0,1,3,2,1,2,1]
        true_answer = 6
        self.assertEqual(trap(height), true_answer)
    def test_2(self):
        height = [4,2,0,3,2,5]
        true_answer = 9
        self.assertEqual(trap(height), true_answer)
if __name__ == '__main__':
    unittest.main()
