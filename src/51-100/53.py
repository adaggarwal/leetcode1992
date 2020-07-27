'''
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

'''

'''
Use Kadane's algorithm which is a DP solution. A running max and a global max would do the trick here. 
'''

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        highVal = runningSum = -sys.maxsize-1
        
        for element in nums:
            runningSum += element
            runningSum = max(element,runningSum)
            if highVal < runningSum:
                highVal = runningSum
                
        return highVal