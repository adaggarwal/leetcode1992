'''

695. Max Area of Island

Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

Find the maximum area of an island in the given 2D array. (If there is no island, the maximum area is 0.)

Example 1:
[[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
Given the above grid, return 6. Note the answer is not 11, because the island must be connected 4-directionally.
Example 2:
[[0,0,0,0,0,0,0,0]]
Given the above grid, return 0.
Note: The length of each dimension in the given grid does not exceed 50.

'''
class Solution:
    def maxAreaOfIsland(self, grid):
        
        #a set to store the elements visited in the past; use a set so that search is O(1)
        visitedNode = set()
        maxArea = 0

        #a stack is needed to store the tuple coordinate values to apply localized DFS on a seed
        stack = []
        
        #traverse through the grid in O(n); n -> elements in the grid (row*column)
        for rowIndex, rowValue in enumerate(grid):
            for columnIndex, columnValue in enumerate(rowValue):

                #skip the elements already visited O(1)
                if (rowIndex, columnIndex) in visitedNode:
                    continue

                localArea = 0

                #only consider the element if the value is non zero
                if columnValue:
                    stack = [(rowIndex, columnIndex)]

                #add it to the visited nodes O(1)
                visitedNode.add((rowIndex, columnIndex))

                #O(~k); k -> ~1 --> elements in the stack; but considering these k elements are
                # visited only once hence; k tends to 1 inside the nested for
                while stack:
                    locRow, locCol = stack.pop()

                    #what if each grid value had a weight to it? so don't solve for value 1s only
                    localArea += grid[locRow][locCol]

                    #try to visit the DFS neighbors of this Seed
                    for neighbor in [(locRow-1, locCol), (locRow+1, locCol), 
                    (locRow, locCol-1), (locRow, locCol+1)]:
                        #before counting the neighbor, validate it
                        if (0 <= neighbor[0] < len(grid)) and (0<= neighbor[1] < len(grid[0])) \
                        and (neighbor not in visitedNode) and (grid[neighbor[0]][neighbor[1]]):

                            #add to the stack and count the node visited so that it is not visited again
                            stack.append(neighbor)
                            visitedNode.add(neighbor)

                #each time the stack is emptied, the area of the island was calculated, update the global maxima
                maxArea = max(maxArea, localArea)
        
        
        return maxArea


x = Solution()
ar = x.maxAreaOfIsland([[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]])

print('Area = {}'.format(ar))