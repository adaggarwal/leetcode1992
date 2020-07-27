'''
153. Find Minimum in Rotated Sorted Array
Medium

741

131

Favorite

Share
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

Find the minimum element.

You may assume no duplicate exists in the array.

Example 1:

Input: [3,4,5,1,2] 
Output: 1
Example 2:

Input: [4,5,6,7,0,1,2]
Output: 0
'''

class Solution:
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return None
        
        l, h= 0, len(nums)-1

        while l<h:
            m= (l+h)//2
            if nums[m]> nums[h]:
                l=m+1
            else:
                h=m
        return nums[l]