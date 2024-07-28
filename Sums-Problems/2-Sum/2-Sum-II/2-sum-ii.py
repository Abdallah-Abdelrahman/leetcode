#!/usr/bin/env python3
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l, r = 0, len(nums) - 1  # Initialize two pointers, left (l) and right (r)

        while l < r:  # Loop until the two pointers meet
            if nums[l] + nums[r] == target:  # Check if the sum of the two numbers equals the target
                return [l + 1, r + 1]  # Return the 1-based indices of the two numbers
            
            if nums[l] + nums[r] < target:  # If the sum is less than the target
                l += 1  # Move the left pointer to the right
        
            if nums[l] + nums[r] > target:  # If the sum is greater than the target
                r -= 1  # Move the right pointer to the left