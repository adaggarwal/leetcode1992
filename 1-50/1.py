'''
This solution is 0(NlogN) as we start by sorting the list
Start with two pointers left and right as the extremes of the list
Add left and right and compare with target
if target is greater than the sum it would make sense to decrease the sum ==> by going lower on the upper bound as it represents the higher weight
similarly, if target is smaller than the sum then increase the left bound which represents the smaller weight
then at the end there is a small hack to safeguard against corner cases; but I agree that can be a little more neat
'''

print("Enter")

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        sorted_num_list = sorted(nums)
        left = 0
        right = len(nums) - 1
        while left<right:
            summ = (sorted_num_list[left]+sorted_num_list[right])
            if summ ==target:
                break
            if summ<target:
                left+=1
            if summ>target:
                right-=1
        num1,num2 = sorted_num_list[left],sorted_num_list[right]
        l,r=-1,-1
        for e in range(0,len(nums)):
            if num1 == nums[e] and l==-1:
                l = e
            elif num2 == nums[e] and r==-1:
                r = e
        return [l,r]
