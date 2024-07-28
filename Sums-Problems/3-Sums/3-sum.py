#!/usr/bin/env python3
from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = set()  # Initialize a set to store unique triplets
        nums.sort()  # Sort the list to facilitate the two-pointer approach

        for i in range(len(nums)):  # Iterate through the list
            if i > 0 and nums[i] == nums[i - 1]:  # Skip duplicate elements
                continue

            l, r = i + 1, len(nums) - 1  # Initialize two pointers, left (l) and right (r)
            while l < r:  # Loop until the two pointers meet
                if nums[i] + nums[l] + nums[r] < 0:  # If the sum is less than zero
                    l += 1  # Move the left pointer to the right
                elif nums[i] + nums[l] + nums[r] > 0:  # If the sum is greater than zero
                    r -= 1  # Move the right pointer to the left
                else:  # If the sum is zero
                    result.add((nums[i], nums[l], nums[r]))  # Add the triplet to the result set
                    l += 1  # Move the left pointer to the right to find new triplets
        return result  # Return the set of unique triplets