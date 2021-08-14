"""
Given a signed 32-bit integer x, return x 
with its digits reversed. If reversing x causes the value to 
go outside the signed 32-bit integer range [-2^31, 2^31 - 1], then return 0.

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


class solution():
    def reverseInteger(x: int) -> int:
        if not isinstance(x, int):
            return " X is different from an integer"
        if x < -2**31 and x > 2**31-1:
            return 0
        strValue= str(x)
        if x < 0:
            return int(strValue[:0:-1])*-1
        else:
            return int(strValue[::-1])

