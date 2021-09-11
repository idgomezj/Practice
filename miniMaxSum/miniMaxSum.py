"""
Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers. Then print the respective minimum and maximum values as a single line of two space-separated long integers.

Example

arr =[1,3,5,7,9]

The minimum sum is 1+3+5+7 = 16  and the maximum sum is 3+5+7+9=24 . The function prints

"""
from typing import List


class miniMaxSum:
    def solve(arr: List) -> str:
        if next((True for x in arr if x < 1 or x > 10**9), False):
            return
        arr.sort()
        return str(sum(arr[:4])) + "  " + str(sum(arr[-4:]))


if "__main__" == __name__:
    print(miniMaxSum.solve([1, 3, 5, 7, 9]))
    print(next((True for x in [1, 3, 5, 7, 9] if x <= 1 or x > 10**9), False))
