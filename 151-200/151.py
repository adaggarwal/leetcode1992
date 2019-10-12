'''

151. Reverse Words in a String
Medium
389
1902


Given an input string, reverse the string word by word.

Example:  

Input: "the sky is blue",
Output: "blue is sky the".
Note:

A word is defined as a sequence of non-space characters.
Input string may contain leading or trailing spaces. However, your reversed string should not contain leading or trailing spaces.
You need to reduce multiple spaces between two words to a single space in the reversed string.
Follow up: For C programmers, try to solve it in-place in O(1) space.

'''
'''

Approach:

1. swap all the characters symmetrically from the middle 
2. perform (1) for each word seperated by space

We then have our python solution with O(1) space and O(n) time. 

For more checkout - https://github.com/adityaaggarwal1992/leetcode1992

'''


class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = s.strip()
        s = list(s)
        for i in range(0, len(s)//2):
            temp = s[i]
            s[i] = s[len(s)-1-i]
            s[len(s)-1-i] = temp
            
        s = [x for x in "".join(s).split(" ") if x]
        
        for ind,element in enumerate(s):
            element = list(element)
            for i in range(0,len(element)//2):
                temp = element[i]
                element[i] = element[len(element)-1-i]
                element[len(element)-1-i] = temp
            s[ind] = "".join(element)
            
        return " ".join(s) 

class Solution:
    def reverseWords(self, s: str) -> str:
        s = " ".join([x for x in s.split(" ") if x])
        s = s[::-1]
        s = s.split(" ")
        for i,e in enumerate(s):
            s[i]= e[::-1]
        return " ".join(s)