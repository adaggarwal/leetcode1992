'''
242. Valid Anagram

Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
Note:
You may assume the string contains only lowercase alphabets.
'''

class Solution:
    
    def countS(self, s):
        count = [0]*26
        strn = ''
        for char in s:
            if not count[ord(char) - ord('a')]:
                count[ord(char) - ord('a')] = 1
            else:
                count[ord(char) - ord('a')] += 1
        for el in range(0,len(count)):
            if count[el]:
                strn += chr(ord('a') + el)*count[el]
        return strn
                
        
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if Solution.countS(self, s) == Solution.countS(self, t): 
            return True
        else:
            return False
