import unittest
import reverseInteger as RI
import timeit


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

py1=timeit.timeit('RI.solution.reverseInteger(321123344)',
                    setup='import reverseInteger as RI',
                    number=10000)
py2=timeit.timeit('RI.solution.reverseInteger(321123344)',
                    setup='import reverseIntegerOpt as RI',
                    number=10000)
cy=timeit.timeit('RI.reverseInteger(321123344)',
                    setup='import reverseInteger_cython as RI',
                    number=10000)
cy2=timeit.timeit('RI.reverseInteger(321123344)',
                    setup='import reverseInteger_cython2 as RI',
                    number=10000)
print(f'Cython1 is {py1/cy} faster than Python model 1')
print(f'Cython1 is {py2/cy} faster than Python optimized model')
print(f'Cython1 is {cy2/cy} faster than Python optimized model')



if __name__=="__main__":
    unittest.main()
