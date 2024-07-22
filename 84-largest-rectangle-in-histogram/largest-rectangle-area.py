class Solution:
    
    def largestRectangleArea(self, heights):
        """
        Args:
        - heights (List[int]): A list of integers representing the heights of bars in the histogram.

        Returns:
        - int: The area of the largest rectangle that can be formed in the histogram.

        Complexity Analysis:
        - Time complexity: O(n), where n is the number of bars in the histogram.
        - Space complexity: O(n) due to the use of the stack.
        """
        maxArea = 0
        stack = []
        heights.append(0)
        
        for i, h in enumerate(heights):
            while stack and heights[stack[-1]] > h:
                idx = stack.pop()
                height = heights[idx]
                width = i - stack[-1] - 1 if stack else i
                maxArea = max(maxArea, height * width)
            stack.append(i)
        return maxArea

    
# Test Run
solution = Solution()
print(solution.largestRectangleArea([2, 1, 5, 6, 2, 3])) # 10
print(solution.largestRectangleArea([2, 4])) # 4
print(solution.largestRectangleArea([2, 1, 2])) # 3