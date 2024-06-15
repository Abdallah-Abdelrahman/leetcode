#!/usr/bin/env python3
'''Module defines leetcode problem.'''
import time
from typing import List
from collections import deque

class Solution:
    '''class `Solution`.'''
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        '''return list of intersect coordinates between
        pacific and atlantic ocean
        '''
        ROWS = len(heights)
        COLS = len(heights[0])

        # find all the values that can reach the pacific
        pacifics = [[False] * COLS for _ in range(ROWS)]
        q = deque()
        for c in range(COLS):
            q.append((0, c))
            pacifics[0][c] = True
        for r in range(1, ROWS):
            q.append((r, 0))
            pacifics[r][0] = True
        while len(q) > 0:
            r, c = q.popleft()
            # up
            if r > 0 and not pacifics[r - 1][c] and heights[r - 1][c] >= heights[r][c]:
                pacifics[r - 1][c] = True
                q.append((r - 1, c))
            # down
            if r < ROWS - 1 and not pacifics[r + 1][c] and heights[r + 1][c] >= heights[r][c]:
                pacifics[r + 1][c] = True
                q.append((r + 1, c))
            # left
            if c > 0 and not pacifics[r][c - 1] and heights[r][c - 1] >= heights[r][c]:
                pacifics[r][c - 1] = True
                q.append((r, c - 1))
            # right
            if c < COLS - 1 and not pacifics[r][c + 1] and heights[r][c + 1] >= heights[r][c]:
                pacifics[r][c + 1] = True
                q.append((r, c + 1))


        # find all the values that can reach the atlantic
        atlantics = [[False] * COLS for _ in range(ROWS)]
        q = deque()
        for c in range(COLS):
            q.append((ROWS - 1, c))
            atlantics[ROWS - 1][c] = True
        for r in range(ROWS - 1):
            q.append((r, COLS - 1))
            atlantics[r][COLS - 1] = True

        while len(q) > 0:
            r, c = q.popleft()
            # up
            if r > 0 and not atlantics[r - 1][c] and heights[r - 1][c] >= heights[r][c]:
                atlantics[r - 1][c] = True
                q.append((r - 1, c))
            # down
            if r < ROWS - 1 and not atlantics[r + 1][c] and heights[r + 1][c] >= heights[r][c]:
                atlantics[r + 1][c] = True
                q.append((r + 1, c))
            # left
            if c > 0 and not atlantics[r][c - 1] and heights[r][c - 1] >= heights[r][c]:
                atlantics[r][c - 1] = True
                q.append((r, c - 1))
            # right
            if c < COLS - 1 and not atlantics[r][c + 1] and heights[r][c + 1] >= heights[r][c]:
                atlantics[r][c + 1] = True
                q.append((r, c + 1))

        # find values that satisfy both
        result = []
        for r in range(ROWS):
            for c in range(COLS):
                # print(r, c, )
                if pacifics[r][c] and atlantics[r][c]:
                    result.append([r, c])


        return result


if __name__ == '__main__':
    start = time.perf_counter()
    matrix = [[10],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]

    res = Solution().pacificAtlantic(matrix)
    print(f'time: {time.perf_counter()-start}\n{res}')
