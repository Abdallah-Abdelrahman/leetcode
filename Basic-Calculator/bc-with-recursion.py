#!/usr/bin/env python3
"""solving the basic calculator problem using recursive function"""

class Solution:
    def calculate(self, s: str) -> int:
        def helper(i):
            num = '0'  # Initialize num as a string to build multi-digit numbers
            res = 0  # Initialize the result
            op = 1  # Initialize the operator, 1 for positive and -1 for negative

            while i < len(s):  # Loop through each character in the string
                curr = s[i]  # Get the current character
                if curr.isdigit():  # If the current character is a digit
                    num += curr  # Append the digit to num
                else:  # If the current character is not a digit
                    res += int(num) * op  # Update the result with the current number and operator
                    num = '0'  # Reset num to '0'
                    if curr in '+-':  # If the current character is '+' or '-'
                        op = 1 if curr == '+' else -1  # Update the operator
                    elif curr == '(':  # If the current character is '('
                        tmp, i = helper(i + 1)  # Recursively call helper for the sub-expression
                        res += tmp * op  # Update the result with the sub-expression result
                    elif curr == ')':  # If the current character is ')'
                        return res, i  # Return the result and the current index
                i += 1  # Move to the next character
            else:  # After the loop ends
                res += int(num) * op  # Add the last number to the result
            return res  # Return the final result

        return helper(0)  # Start the helper function from index 0