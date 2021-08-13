import unittest
import reverseInteger as RI

"""
Example 1:
    Input: x = 123
    Output: 321
Example 2:
    Input: x = -123
    Output: -321
Example 3:
    Input: x = 120
    Output: 21

Example 4:
    Input: x = 0
    Output: 0

"""
class TestReverseInteger(unittest.TestCase):
    def test_reverseInteger(self):
        self.assertEqual(RI.solution.reverseInteger(321),123)
        self.assertEqual(RI.solution.reverseInteger(-123),-321)
        self.assertEqual(RI.solution.reverseInteger(120),21)
        self.assertEqual(RI.solution.reverseInteger(0),0)

if __name__=="__main__":
    unittest.main()
