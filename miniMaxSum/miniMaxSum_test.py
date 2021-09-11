import unittest
import miniMaxSum as MM

"""
Input [1,3,5,7,9]

Output 16 24

Input [1,2,3,4,5]
Output 10 14

"""


class TestMiniMaxSum(unittest.TestCase):
    def test_miniMaxSum(self):
        self.assertEqual(MM.miniMaxSum().solve([1, 3, 4, 7, 9]), "16 24")
        self.assertEqual(MM.miniMaxSum().solve([1, 2, 3, 4, 5]), "10 14")


if __name__ == "__main__":
    unittest.main()
