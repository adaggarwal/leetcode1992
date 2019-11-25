'''
The first solution is 0(NlogN) as we start by sorting the list
Start with two pointers left and right as the extremes of the list
Add left and right and compare with target
if target is greater than the sum it would make sense to decrease the sum ==> by going lower on the upper bound as it represents the higher weight
similarly, if target is smaller than the sum then increase the left bound which represents the smaller weight
then at the end there is a small hack to safeguard against corner cases; but I agree that can be a little more neat
'''

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        #this is the problem that you need to sort in this method
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

'''
    Second method : hash table with one pass O(n)
'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictionary = dict()
        #loop through the list and add elements to the dict
        #check if the element's counterpart is already in the dictionary
        for index,element in enumerate(nums):
            if (target-element) in dictionary:
                return [index, dictionary[target-element]]
            else:
                dictionary[element] = index
