#!/usr/bin/env python3
"""solving the basic calculator problem using a stack"""

class Solution:
    def calculate(self, s: str) -> int:
        num = '0'  # Initialize num as a string to build multi-digit numbers
        res = 0  # Initialize the result
        op = 1  # Initialize the operator, 1 for positive and -1 for negative
        stack = []  # Initialize the stack to handle parentheses
        i = 0  # Initialize the index for the input string

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
                    stack.append([res, op])  # Push the current result and operator onto the stack
                    res = 0  # Reset the result for the new sub-expression
                    op = 1  # Reset the operator for the new sub-expression
                elif curr == ')':  # If the current character is ')'
                    prev_res, prev_op = stack.pop()  # Pop the previous result and operator from the stack
                    res = prev_res + res * prev_op  # Update the result with the sub-expression result
            i += 1  # Move to the next character
        else:  # After the loop ends
            res += int(num) * op  # Add the last number to the result
        return res  # Return the final result