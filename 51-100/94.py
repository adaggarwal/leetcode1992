'''

94. Binary Tree Inorder Traversal
Medium

1231

51

Favorite

Share
Given a binary tree, return the inorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,3,2]
Follow up: Recursive solution is trivial, could you do it iteratively?

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


#iteratively:

class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        stack = []
        current = root
        vals = []
        while stack or current:
            while current:
                stack.append(current)
                current = current.left
            current = stack.pop()
            vals.append(current.val)
            current = current.right
        return vals

#recursive:

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        inorderList = []
        Solution.inorder(root, inorderList)
        return inorderList

    def inorder(Node, inList):
        if not Node:
            return
        else:
            Solution.inorder(Node.left, inList)
            inList.append(Node.val)
            Solution.inorder(Node.right, inList)