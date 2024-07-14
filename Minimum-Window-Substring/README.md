# Minimum Window Substring

Given two strings `s` and `t` of lengths `m` and `n` respectively, return the minimum window 
substring of `s` such that every character in `t` (including duplicates) is included in the window. If there is no such substring, return the empty string `""`.

The testcases will be generated such that the answer is unique.


## Examples:

Input: `s = "ADOBECODEBANC", t = "ABC"`
Output: `"BANC"`
Explanation: The minimum window substring `"BANC"` includes `'A'`, `'B'`, and `'C'` from string `t`.
Output: `[1,1,2,3,4,4,5,6]`


Input: `s = "a", t = "a"`
Output: `"a"`
Explanation: The entire string `s` is the minimum window.

Input: `s = "a", t = "aa"`
Output: `""`
Explanation: Both `'a'`s from `t` must be included in the window.
Since the largest window of `s` only has one `'a'`, return empty string.

## Difficulty:

`hard`

## Learning Objectives:

+ Hash Table
+ String
+ Sliding Window

## Link:

[problem on leetcode](https://leetcode.com/problems/minimum-window-substring/)
