import unittest
import staircase as ST

"""
Input (stdin)= 6

Your Output (stdout)

     #
    ##
   ###
  ####
 #####
######
"""


class TestReverseInteger(unittest.TestCase):
    def test_reverseInteger(self):
        self.assertEqual(ST.staircase().solve(
            6), "     #\n    ##\n   ###\n  ####\n #####\n######")


if __name__ == "__main__":
    unittest.main()
