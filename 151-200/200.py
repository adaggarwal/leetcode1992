'''

200. Number of Islands

Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input:
11110
11010
11000
00000

Output: 1
Example 2:

Input:
11000
11000
00100
00011

Output: 3

'''



class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        
        visited = set()
        stack = []
        islandNo = 0

        for row, rval in enumerate(grid):
            for col, cval in enumerate(rval):
                if ((row, col) in visited) or (int(cval) == 0):
                    continue
        
                visited.add((row, col))
                stack.append((row, col))
                
                while stack:
                    
                    seed = stack.pop()
                    neighbors = [(seed[0]-1, seed[1]),(seed[0]+1, seed[1]),\
                    (seed[0], seed[1]-1),(seed[0], seed[1]+1)]
                    
                    for nei in neighbors:
                        if (0<= nei[0] < len(grid)) and ( 0<= nei[1] < len(grid[0]) ) and int(grid[nei[0]][nei[1]]) and (nei not in visited):
                
                            
                            stack.append(nei)
                            visited.add(nei)

                islandNo += 1                

        return islandNo