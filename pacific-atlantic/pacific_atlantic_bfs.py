#!/usr/bin/env python3
'''Module defines leetcode problem.'''
import time
from typing import List, Tuple, Deque
from collections import deque


class Solution:
    '''class `Solution`.'''
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        '''return list of intersect coordinates between
        pacific and atlantic ocean
        '''
        ROWS = len(heights)
        COLS = len(heights[0])

        # default values of pacific
        pacifics = [[False] * COLS for _ in range(ROWS)]
        # default values of atlantic
        atlantics = [[False] * COLS for _ in range(ROWS)]
        q = deque()
        # pacific top borders
        self.mark_borders(pacifics, COLS, False, q, 0)
        # pacific left borders
        self.mark_borders(pacifics, ROWS, True, q, 0, start=1)

        self.traverse(heights, pacifics, q)

        q = deque()
        # atlantic bottom borders
        self.mark_borders(atlantics, COLS, False, q, ROWS-1)
        # pacific right borders
        self.mark_borders(atlantics, ROWS-1, True, q, COLS-1)

        self.traverse(heights, atlantics, q)

        # find values that satisfy both
        result = []
        for r in range(ROWS):
            for c in range(COLS):
                # print(r, c, )
                if pacifics[r][c] and atlantics[r][c]:
                    result.append([r, c])

        return result

    def traverse(
            self,
            heights: List[List[int]],
            ocean: List[List[bool]],
            queue: Deque[Tuple[int, int]]):
        '''traverse grid to mark cell as pacific/atlantic'''
        while len(queue) > 0:
            r, c = queue.popleft()

            if (
                    r > 0
                    and not ocean[r-1][c]
                    and heights[r-1][c] >= heights[r][c]
                    ):
                # up
                queue.append((r-1, c))
                ocean[r-1][c] = True
            if (
                    c < len(heights[0]) - 1
                    and not ocean[r][c + 1]
                    and heights[r][c+1] >= heights[r][c]
                    ):
                # right
                queue.append((r, c+1))
                ocean[r][c+1] = True
            if (
                    r < len(heights) - 1
                    and not ocean[r+1][c]
                    and heights[r+1][c] >= heights[r][c]
                    ):
                # bottom
                queue.append((r+1, c))
                ocean[r+1][c] = True
            if (
                    c > 0
                    and not ocean[r][c-1]
                    and heights[r][c-1] >= heights[r][c]
                    ):
                # left
                queue.append((r, c-1))
                ocean[r][c-1] = True

    def mark_borders(
            self,
            ocean: List[List[bool]],
            height: int,
            is_col: bool,
            q: Deque[Tuple[int, int]],
            idx: int,
            start: int = 0) -> None:
        '''marks ocean borders (pacific or atlantic)'''
        for i in range(start, height):
            if is_col:
                ocean[i][idx] = True
                q.append((i, idx))
            else:
                ocean[idx][i] = True
                q.append((idx, i))


if __name__ == '__main__':
    start = time.perf_counter()
    matrix = [[1, 2, 3], [8, 9, 4], [7, 6, 5]]

    res = Solution().pacificAtlantic(matrix)
    print(f'time: {time.perf_counter()-start}\n{res}')
