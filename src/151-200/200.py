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

# Approach 1 - BFS

# Time - O(row*column)
# Space - O(row*column) -- This can be O(1) if input matrix is changed 

class Solution:
    
    def getNeighbors(self, coordinate) -> list:
        row,col = coordinate
        return [(row-1,col), (row,col-1), (row+1,col), (row,col+1)]
    
    def isValid(self, coordinate, grid) -> bool:
        row,col = coordinate
        if (0<=row<len(grid)) and (0<=col<len(grid[0])):
            return True
        return False
    
    def isLand(self, coordinate, grid) -> bool:
        row, col = coordinate
        if grid[row][col] == "1":
            return True
        return False
    
    def bfs(self,row,col,visited,grid) -> None:
        queue = deque([(row,col)])
        visited.add((row,col))
        while queue:
            for _ in range(len(queue)):
                seed = queue.pop()
                nList = self.getNeighbors(seed)
                for element in nList:
                    if self.isValid(element, grid) and self.isLand(element, grid) and (element not in visited):
                        queue.append(element)
                        visited.add(element)
    
    def numIslands(self, grid: List[List[str]]) -> int:
        if (not grid) or (not grid[0]):
            return 0
        islands = 0
        visited = set()
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if (grid[row][col] == "0") or ((row,col) in visited):
                    continue
                self.bfs(row,col,visited,grid)
                islands += 1
        return islands