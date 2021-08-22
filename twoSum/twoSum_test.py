import unittest
import timeit
import twoSumExercise as ts
import twoSumExercise2 as ts2
"""
Example
Given nums = [2,7,11,15], target = 9
Return [0,1]

"""


class TestTwoSum(unittest.TestCase):
    def test_twoSum(self):
        self.assertListEqual(ts.twoSum([2, 7, 11, 15], 9), [0, 1])
        self.assertListEqual(ts.twoSum([2, 7, 11, 15, 20, 25], 35), [3, 4])
        self.assertEqual(ts.twoSum([2, 7, 11, 15, 20, 25], 25), None)
        self.assertEqual(ts.twoSum([2, 7, 11, 15, 20, 25], 250), None)
        self.assertEqual(ts.twoSum(), None)

    def test_twoSum2(self):
        self.assertListEqual(ts2.twoSum([2, 7, 11, 15], 9), [0, 1])
        self.assertListEqual(ts2.twoSum([2, 7, 11, 15, 20, 25], 35), [3, 4])
        self.assertEqual(ts2.twoSum([2, 7, 11, 15, 20, 25], 25), None)
        self.assertEqual(ts2.twoSum([2, 7, 11, 15, 20, 25], 250), None)
        self.assertEqual(ts2.twoSum(), None)


py1 = timeit.timeit('ts.twoSum([2, 7, 11, 15, 20, 25], 35)',
                    setup='import twoSumExercise as ts',
                    number=10000)
py2 = timeit.timeit('ts2.twoSum([2, 7, 11, 15, 20, 25], 35)',
                    setup='import twoSumExercise2 as ts2',
                    number=10000)

print(f'Py1 is {py2/py1} faster than Python model py2')
if __name__ == "__main__":
    unittest.main()
