#!/usr/bin/env python3
from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res, temp = [], []  # Initialize result list and temporary list for current combination
        length = len(nums)  # Get the length of the input list
        nums.sort()  # Sort the input list to facilitate the k-sum approach

        def twoSum(target: int, l: int) -> List[int]:
            r = len(nums) - 1  # Initialize the right pointer
            while l < r:  # Loop until the two pointers meet
                if nums[l] + nums[r] < target:  # If the sum is less than the target
                    l += 1  # Move the left pointer to the right
                elif nums[l] + nums[r] > target:  # If the sum is greater than the target
                    r -= 1  # Move the right pointer to the left
                else:  # If the sum is equal to the target
                    res.append(temp + [nums[l], nums[r]])  # Add the current combination to the result
                    l += 1  # Move the left pointer to the right
                    while l < r and nums[l] == nums[l - 1]:  # Skip duplicate elements
                        l += 1

        def kSum(target, k, start):
            if k == 2:  # Base case: if k is 2, use the twoSum function
                twoSum(target, start)
            else:
                for i in range(start, length - k + 1):  # Iterate through the list
                    if i > start and nums[i] == nums[i - 1]:  # Skip duplicate elements
                        continue
                    temp.append(nums[i])  # Add the current element to the temporary list
                    kSum(target - nums[i], k - 1, i + 1)  # Recursively call kSum with reduced k and target
                    temp.pop()  # Remove the last element from the temporary list

        kSum(target, 4, 0)  # Start the kSum function with k=4
        return res  # Return the result list