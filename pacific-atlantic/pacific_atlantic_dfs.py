#!/usr/bin/env python3
import time
'''Module defines leetcode problem.
Difficulty:
    medium
Description:
    There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean.
    The Pacific Ocean touches the island's left and top edges,
    and the Atlantic Ocean touches the island's right and bottom edges.

    The island is partitioned into a grid of square cells.
    You are given an m x n integer matrix heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).
 
    The island receives a lot of rain, and the rain water can flow to neighboring cells directly north,
    south, east, and west if the neighboring cell's height is less than or equal to the current cell's height.
    Water can flow from any cell adjacent to an ocean into the ocean.
    
    Return a 2D list of grid coordinates result,
    where result[i] = [ri, ci] denotes that rain water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.
'''


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
