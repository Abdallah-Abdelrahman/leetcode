#!/usr/bin/env python3
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}  # Initialize a dictionary to store the indices of the elements
        for i in range(len(nums)):  # Iterate through the list of numbers
            res = target - nums[i]  # Calculate the complement of the current number
            if res not in hash:  # If the complement is not in the dictionary
                hash[nums[i]] = i  # Add the current number and its index to the dictionary
            else:
                return [hash[res], i]  # If the complement is found, return the indices
        return []  # Return an empty list if no solution is found