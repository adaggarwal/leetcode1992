# 96. Unique Binary Search Trees
# Share
# Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?

# Example:

# Input: 3
# Output: 5
# Explanation:
# Given n = 3, there are a total of 5 unique BST's:

#    1         3     3      2      1
#     \       /     /      / \      \
#      3     2     1      1   3      2
#     /     /       \                 \
#    2     1         2                 3
 

# Constraints:

# 1 <= n <= 19

'''
Approach:
Dynamic Programming – Memoization
1.	Create a hash that stores the solutions for each subproblem
2.	This problem has to do with calculating Catalan's numbers
3.	For 0 and 1 we return the result as 1. For case 2, we can only create two cases
  a.	For case 3 – we have {1,2,3} as our options. When we pick 1 as root; we have {2,3} for the right subtree and {} for the left. 
    i.	When we pick 2, we have one choice for left and one choice for right subtree
    ii.	When we pick 3, we have {1,2} as the choices for left subtree and {} for the right subtree. 
    iii.	For these three different cases, we take the cartesian product of the left and right subtrees’ solutions. For {1,2} the value of n is 2 and solution when n=2 is 2. 
    iv.	Hence for n=3; we have 1*2+1*1+2*1 = 5
4.	Using the intuition in pt 3, it is easy to formulate a loop and calculate the possible number of subtrees. 
5.	Saving each small solution from 1….n makes this approach faster and hence a DP approach.

Time – O(n^2)
Space – O(n) 

'''

class Solution:
    def numTrees(self, n: int) -> int:
        hashM = {}
        def numT(n):
            if n==0 or n==1:
                return 1
            # nonlocal hashM
            if n in hashM:
                return hashM[n]
            total = 0
            for i in range(1,n+1):
                total += numT(n-i)*numT(i-1)
            hashM[n] = total
            return total
        return numT(n)