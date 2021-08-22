"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that eacg input would have exactly one solution, and you may not use the same element twice

Example
Given nums = [2,7,11,15], target = 9
Return [0,1]
"""
from typing import List


def twoSum(data: List[int] = None, target: int = None) -> List[int]:
    if not data or not target:
        return
    listComplement = {}
    for i, num in enumerate(data):
        if target - num in listComplement:
            return [listComplement[target-num], i]
        elif num not in listComplement:
            listComplement[num] = i
