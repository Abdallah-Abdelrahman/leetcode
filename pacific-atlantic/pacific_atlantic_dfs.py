#!/usr/bin/env python3
import time
'''Module defines leetcode problem.'''


class Solution:
    '''class `Solution`.'''
    def pacificAtlantic(self, heights):
        '''return list of intersect coordinates between
        pacific and atlantic ocean
        '''
        m, n = len(heights), len(heights[0])
        directions = [(0,1), (0,-1), (1,0), (-1,0)]

        def dfs(x, y, visited):
            visited.add((x, y))
            # print(visited)
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in visited and heights[nx][ny] >= heights[x][y]:
                    dfs(nx, ny, visited)

        pacific, atlantic = set(), set()

        # add pacific columns
        # add atlantic columns
        for i in range(m):
            dfs(i, 0, pacific)
            dfs(i, n-1, atlantic)

        # add pacific rows
        # add atlantic rows
        for i in range(n):
            dfs(0, i, pacific)
            dfs(m-1, i, atlantic)

        return list(pacific & atlantic)


if __name__ == '__main__':
    start = time.perf_counter()
    matrix = [[10],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]

    res = Solution().pacificAtlantic(matrix)
    print(f'time: {time.perf_counter()-start}\n{res}')
