'''
230. Kth Smallest Element in a BST

Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

Note: 
You may assume k is always valid, 1 = k = BST's total elements.

Example 1:

Input: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
Output: 1
Example 2:

Input: root = [5,3,6,2,4,null,null,1], k = 3
       5
      / \
     3   6
    / \
   2   4
  /
 1
Output: 3
Follow up:
What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently? How would you optimize the kthSmallest routine?

Intention:
    1. The question requires to modify the tree into a list of some sort of sorted order list and return the k index entry.
    2. Simply perform an inorder traversal and keep saving the elements in an array as they come by. 
    3. return the (k-1)th index of this list.

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    def inorder(self, root, ret):
        if not root:
            return None
        Solution.inorder(self, root.left, ret)
        ret.append(root.val)
        Solution.inorder(self, root.right, ret)
        return ret
    
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        ret = []
        ret = Solution.inorder(self, root, ret)
        return ret[k-1]
