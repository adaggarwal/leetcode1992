# 54. Spiral Matrix
# Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

# Example 1:

# Input:
# [
#  [ 1, 2, 3 ],
#  [ 4, 5, 6 ],
#  [ 7, 8, 9 ]
# ]
# Output: [1,2,3,6,9,8,7,4,5]
# Example 2:

# Input:
# [
#   [1, 2, 3, 4],
#   [5, 6, 7, 8],
#   [9,10,11,12]
# ]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]

'''
Space - O(1) if output is not considered
Time - O(row*col)

row*col = number of elements in the input matrix
'''


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if len(matrix) < 1:
            return []
        
        # start with an empty result list
        resultList = []
        
        # define boundaries
        left, right, upper, bottom = 0, len(matrix[0]) -1, 0, len(matrix)-1
        
        # exit condition
        while len(resultList)<(len(matrix)*len(matrix[0])):
            
            if upper<=bottom:
                #left to right --> step size '+' -- row constant -- col variable
                for i in range(left, right+1, 1):
                    resultList.append(matrix[upper][i])
            
            upper +=1
            
            if left<=right:
                #top to bottom --> step size '+' -- row variable -- col constant
                for i in range(upper, bottom+1, 1):
                    resultList.append(matrix[i][right])
                
            right -=1
            
            if upper<=bottom:
                #left to right --> step size '-' -- row constant -- col variable
                for i in range(right, left-1, -1):
                    resultList.append(matrix[bottom][i])

            bottom -= 1
            
            
            if left<=right:
                #left to right --> step size '-' -- row varaible -- col constant
                for i in range(bottom, upper-1, -1):
                    resultList.append(matrix[i][left])
            
            left += 1
            
        return resultList