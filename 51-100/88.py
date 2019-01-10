'''
88. Merge Sorted Array
Easy

839

2278

Favorite

Share
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:

The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.
Example:

Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

Output: [1,2,2,3,5,6]
'''

'''

Approach ->

1. The trick as mentioned in the the hints is to fill the nums1 array from the end. It's a very helpful tip. Let's see how
2. while comparing nums1 and nums2; whenever nums1 is larger then nums2; we can copy the value to as far as the current distance of nums1 + nums2's distance from origin.
3. in case nums1 is less than or equal to nums2; nums2 value will be copied to the same position as aforementioned in (2)
Why does this work?
--> After careful analysis, it will be evident that we are displacing the elements in 1 to make space for elements incoming for 2

For more solutions, visit -> https://github.com/adityaaggarwal1992/leetcode1992

'''

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        a, b = m-1, n-1
        while a>=0 and b>=0:
            if nums1[a] > nums2[b]:
                nums1[a+b+1] = nums1[a]
                a -= 1
            else:
                nums1[a+b+1] = nums2[b]
                b -= 1
            # print(nums1)
        if b>=0:
            nums1[:b+1] = nums2[:b+1]