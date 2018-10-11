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