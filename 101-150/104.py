'''
104. Maximum Depth of Binary Tree

Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its depth = 3.

1. if the Node is None, simply return 0 
2. now recurse through left and add 1 for each non-none nodes
3. same with right sub-tree
4. return the max of both values

'''


'''

Time Complexity - O(n)
Space Complexity - O(n)

'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root==None:
            return 0
        htl = 1 + Solution.maxDepth(self, root.left)
        htr = 1 + Solution.maxDepth(self, root.right)
        
        return max(htl,htr)

class Solution:
    def maxDepth(self, root: TreeNode):
        maxDep = 0
        
        def maxD(r: TreeNode, depth = 0) -> int:
            if not r:
                return 
            depth += 1
            nonlocal maxDep 
            maxDep = max(maxDep, depth)
            maxD(r.left, depth)
            maxD(r.right, depth)
            
        maxD(root)
        return maxDep

