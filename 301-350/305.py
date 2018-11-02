'''
305. Number of Islands II

A 2d grid map of m rows and n columns is initially filled with water. We may perform an addLand operation which turns the water at position (row, col) into a land. Given a list of positions to operate, count the number of islands after each addLand operation. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example:

Input: m = 3, n = 3, positions = [[0,0], [0,1], [1,2], [2,1]]
Output: [1,1,2,3]
Explanation:

Initially, the 2d grid grid is filled with water. (Assume 0 represents water and 1 represents land).

0 0 0
0 0 0
0 0 0
Operation #1: addLand(0, 0) turns the water at grid[0][0] into a land.

1 0 0
0 0 0   Number of islands = 1
0 0 0
Operation #2: addLand(0, 1) turns the water at grid[0][1] into a land.

1 1 0
0 0 0   Number of islands = 1
0 0 0
Operation #3: addLand(1, 2) turns the water at grid[1][2] into a land.

1 1 0
0 0 1   Number of islands = 2
0 0 0
Operation #4: addLand(2, 1) turns the water at grid[2][1] into a land.

1 1 0
0 0 1   Number of islands = 3
0 1 0
Follow up:

Can you do it in time complexity O(k log mn), where k is the length of the positions?
'''

class Solution:
    def numIslands2(self, m, n, positions):
        """
        :type m: int
        :type n: int
        :type positions: List[List[int]]
        :rtype: List[int]
        """
        parentHash, elementId = {}, 1
        islands, resultL = set(), []

        #traverse all the positions
        for x,y in positions:
            #initialize the point with an Id; initialize the same id with itself as the parent
            parentHash[(x,y)] = elementId
            parentHash[elementId] = elementId
            #now traverse all the unit distance neighbors
            neighbors = [(x-1, y), (x+1, y), (x, y+1), (x, y-1)]
            for neighbor in neighbors:
                #if neighbor is already in the hash; we need to unify this element to the parent of the neighbor
                if neighbor in parentHash:
                    parentofNeighbor = Solution.getParent(parentHash[neighbor], parentHash)
                    islands.discard(parentofNeighbor)
                    #compress the parent; make a common parent
                    parentHash[parentofNeighbor] = elementId
            islands.add(elementId)
            resultL.append(len(islands))
            elementId += 1
        return resultL 
    
    def getParent(element, parentHash):
        if element != parentHash[element]:
            parentHash[element] = Solution.getParent(parentHash[element], parentHash)
        return parentHash[element]