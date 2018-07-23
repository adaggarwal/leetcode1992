'''
872. Leaf-Similar Trees

Consider all the leaves of a binary tree.  From left to right order, the values of those leaves form a leaf value sequence.



For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).

Two binary trees are considered leaf-similar if their leaf value sequence is the same.

Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.

 

Note:

Both of the given trees will have between 1 and 100 nodes.
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    def get_leaf_nodes(self, node, leafs):          
        if node is not None:
            if not node.left and not node.right:
                leafs.append(node.val)
            if node.left:
                Solution.get_leaf_nodes(self, node.left, leafs)
            if node.right:
                Solution.get_leaf_nodes(self, node.right, leafs) 
        return leafs
    
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        r1n = Solution.get_leaf_nodes(self, root1, [])
        r2n = Solution.get_leaf_nodes(self, root2, [])
        return r1n == r2n
