#!/usr/bin/env python3
'''Module define solution to Minimum Window Substring'''

class Solution:
    # Initialize pointers and minimum window variables
    def minWindow(self, s: str, t: str) -> str:
        l = 0
        r = 0
        minimum_start = 0
        minimum_length = len(s) + 1
        t_map = {}

        # Populate t_map with characters from t
        for el in t:
            t_map[el] = t_map.get(el, 0) + 1

        count = len(t)

        # Expand the window to the right
        while r < len(s):
            if s[r] in t:
                if t_map.get(s[r], 0) > 0:
                    count -= 1
                t_map[s[r]] -= 1
            r += 1

            # When all characters in t are found in the current window
            while count == 0:
                if r - l < minimum_length:
                    minimum_start = l
                    minimum_length = r - l
                if s[l] in t_map:
                    t_map[s[l]] += 1
                    if t_map.get(s[l], 0) > 0:
                        count += 1
                l += 1

        # Return the minimum window or "" if not found
        return "" if minimum_length == len(s) + 1 else s[minimum_start:minimum_start+minimum_length]