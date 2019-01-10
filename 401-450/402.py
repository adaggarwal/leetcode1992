'''

402. Remove K Digits
Medium
674
33


Given a non-negative integer num represented as a string, remove k digits from the number so that the new number is the smallest possible.

Note:
The length of num is less than 10002 and will be ≥ k.
The given num does not contain any leading zero.
Example 1:

Input: num = "1432219", k = 3
Output: "1219"
Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.
Example 2:

Input: num = "10200", k = 1
Output: "200"
Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.
Example 3:

Input: num = "10", k = 2
Output: "0"
Explanation: Remove all the digits from the number and it is left with nothing which is 0.

'''

'''
Approach 

-> O(n) solution by using stack

Let's use an example "1432219" and k=3

1. Move left to write and the intent is to push each number to the stack
2. Each time we push a number to stack and its not empty and k is greater than 0; we can also exempt the number before current pointer. 
This can be done only when the previous number deems to be bigger than the current. In case that is the case, we can remove the prev 
recursively while k>0.
3. As soon as k==0; we have removed the digits we wished to. 

This was the meat of the logic.
Now let's think about some other cases
1. what if numbers are in increasing order? Well, each prev number would be smaller than current. In that case, we will have all the numbers 
in the stack, isn't it?
--> So, let's evict these big numbers from the end of the stack as they will be the largest and good candidates. Or i should say the best ones.

2. Trailing 0s? Well this is one the nuance of this question, so we can have a filter to remove the unwanted 0s. Depending on the language 
of comfort, this can be done in many ways. And my way may not be the best, but it works. :)

For more python solutions to other leetcode problems. Be sure to checkout -> https://github.com/adityaaggarwal1992/leetcode1992 and even 
feel free to contribute. 

Cheers!!

'''

class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        stack = []
        for element in num:
            while k>0 and stack and int(stack[-1]) > int(element):
                stack.pop()
                k-=1
            stack.append(element)
        stack = stack[0:len(stack)-k]
        temp = 0
        while temp<len(stack) and int(stack[temp]) ==0 :            
            temp += 1
        return "".join(stack[temp:]) if len(stack[temp:]) else "0"
        
        
