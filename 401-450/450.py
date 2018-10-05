'''
450. Delete Node in a BST

Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node reference (possibly updated) of the BST.

Basically, the deletion can be divided into two stages:

Search for a node to remove.
If the node is found, delete the node.
Note: Time complexity should be O(height of tree).

Example:

root = [5,3,6,2,4,null,7]
key = 3

    5
   / \
  3   6
 / \   \
2   4   7

Given key to delete is 3. So we find the node with value 3 and delete it.

One valid answer is [5,4,6,2,null,null,7], shown in the following BST.

    5
   / \
  4   6
 /     \
2       7

Another valid answer is [5,2,6,null,4,null,7].

    5
   / \
  2   6
   \   \
    4   7

'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    def findMax(self,root):
        if root==None:
            return root
        if root.right == None:
            return root
        else:
            return Solution.findMax(self, root.right)
        
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        if root == None:
            return root
        elif root.val<key:
            root.right = Solution.deleteNode(self, root.right, key)
        elif root.val>key:
            root.left = Solution.deleteNode(self, root.left, key)
        else:
            #case 1: where root is the leaf node
            if not root.left and not root.right:
                print("DB1",root.val)
                root = None
            #case 2: where root is not a binary tree
            elif root.left and not root.right:
                print("DB2", root.val)
                root = root.left
            elif root.right and not root.left:
                print("DB3", root.val)
                root = root.right
            #case 3: where root is the binary tree
            else:
                print("DB4",root.val)
                root.val = Solution.findMax(self, root.left).val
                root.left = Solution.deleteNode(self, root.left, root.val)
        return root
