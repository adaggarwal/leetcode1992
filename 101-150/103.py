'''
103. Binary Tree Zigzag Level Order Traversal
Medium
Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

'''

Approach - Two stack
1. The meat of the logic comes to this simple design intent of touching nodes in a fashion that the spiral traversal takes place. 
2. If we use queue and grab elements left to right; we have a simple level order traversal. Here instead we use two stacks. 
3. For stack 1 we maintain a cofiguration where left child is appended before the right child. We essentially are stacking the elements in a way that when we pop them; they get popped
from right to left. 
4. The configuration is exactly the opposite for stack 2. Hence, when we pop nodes, it happens from left to right. 
5. When the node is flushed, the value is stored in a temporary list. 
6. This list is appended to the resultant list of list each time any stack is emptied completely. 

For more solutions visit - https://github.com/adityaaggarwal1992/leetcode1992

'''

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result, temp, s1, s2 = [], [], [], []
        s1.append(root)
        while s1 or s2:
            while s1:
                current = s1.pop()
                if current:
                    s2.append(current.left)
                    s2.append(current.right)
                    temp.append(current.val)
            if temp: result.append(temp)
            temp = []
            while s2:
                current = s2.pop()
                if current:
                    s1.append(current.right)
                    s1.append(current.left)
                    temp.append(current.val)
            if temp: result.append(temp)
            temp = []
        return result     