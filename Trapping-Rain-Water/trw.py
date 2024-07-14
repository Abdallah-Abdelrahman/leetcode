from typing import List


class Solution:
    def trap(self, h: List[int]) -> int:
        left = 0  # Initialize left pointer
        right = len(h) - 1  # Initialize right pointer

        left_max = h[left]  # Initialize max height from the left
        right_max = h[right]  # Initialize max height from the right

        counter = 0  # Initialize water trapped counter

        # Loop until the left pointer is less than the right pointer
        while left < right:
            # If height at left is less than height at right
            if h[left] < h[right]:
                # If current left height is greater than left_max, update left_max
                if h[left] > left_max:
                    left_max = h[left]
                else:
                    # Else, water can be trapped, add to counter
                    counter += left_max - h[left]
                left += 1  # Move left pointer to the right
            else:
                # If current right height is greater than right_max, update right_max
                if h[right] > right_max:
                    right_max = h[right]
                else:
                    # Else, water can be trapped, add to counter
                    counter += right_max - h[right]
                right -= 1  # Move right pointer to the left
        return counter  # Return the total water trapped