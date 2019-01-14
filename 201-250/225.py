'''
255. Verify Preorder Sequence in Binary Search Tree
Medium

274

38

Favorite

Share
Given an array of numbers, verify whether it is the correct preorder traversal sequence of a binary search tree.

You may assume each number in the sequence is unique.

Consider the following binary search tree: 

     5
    / \
   2   6
  / \
 1   3
Example 1:

Input: [5,2,6,1,3]
Output: false
Example 2:

Input: [5,2,1,3,6]
Output: true
Follow up:
Could you do it using only constant space complexity?
'''

class Solution(object):
    def verifyPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: bool
        """
        stk = []
        root = -sys.maxsize-1
        for val in preorder:
            if val<root:
                return False
            
            while stk and stk[-1]<val:
                root = stk.pop()
            
            stk.append(val)
            
        return True