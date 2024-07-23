# 84. Largest Rectangle in Histogram

Given an array of integers `heights` representing the heights of bars in a histogram where the width of each bar is 1, you need to find the area of the largest rectangle that can be formed in the histogram.

**_Description_**:

Given an array `heights` of size `n`, each element `heights[i]` represents the height of the bar charted at position `i`. The width of each bar is assumed to be 1 unit. Your task is to compute the area of the largest rectangle in the histogram formed by these bars.

## Example:

_Input_: `heights = [2,1,5,6,2,3]`

_Output_: `10`

_Explanation_: 

The below image is a histogram where width of each bar is 1.
The largest rectangle is shown in the red area, which has an area = 10 units.

![example ](https://assets.leetcode.com/uploads/2021/01/04/histogram.jpg)

Constraints:

    1 <= heights.length <= 105
    0 <= heights[i] <= 104


## Solution Approach:
To solve this problem efficiently, we can use a stack-based approach that helps in determining the largest rectangle's area at each histogram bar. Here's a step-by-step explanation of the approach:

1. **Initialization**:
   - Use a stack to keep track of indices of the histogram bars in non-decreasing order of their heights.
   - Append a `0` at the end of the `heights` array to handle the case when all bars are in increasing order and to flush out all bars in the stack at the end of processing.

2. **Iterate through the Heights**:
   - Traverse each bar's height in the `heights` array.
   - For each bar, check if it's shorter than the bar at the index stored at the top of the stack. If so, pop the stack and calculate the area of the rectangle using the popped bar's height as the smallest height rectangle possible with its width extending to the current index minus the next top of the stack minus one.
   - Keep track of the maximum area encountered during this process.

3. **Calculate and Update Maximum Area**:
   - The maximum area is updated whenever a rectangle of larger area is found during the iteration.

4. **Return the Result**:
   - After iterating through all bars in the histogram, return the maximum area calculated.

## Complexity Analysis:
    - Time complexity: O(n), where n is the number of bars in the histogram.
    - Space complexity: O(n) due to the use of the stack.

## Learning Objectives:
   - Monotonic stack.

## Link:

[Leetcode Link](https://leetcode.com/problems/largest-rectangle-in-histogram/description/)

[Monotonic Stack](https://en.wikipedia.org/wiki/Monotone_priority_queue)
