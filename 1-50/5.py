# 5. Longest Palindromic Substring
# Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

# Example 1:
# Input: "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.

# Example 2:
# Input: "cbbd"
# Output: "bb"

'''
BRUTE FORCE SOLUTION:

Find all the possible indices and check if they are palindromes
Keep updating the longest palindrome found
Return the longest palindrom
'''

class Solution:
    
    @staticmethod
    def isPalindrome(s: str) -> bool:
        for i in range(0,len(s)//2):
            if s[i] != s[len(s)-1-i]:
                return False
        return True
    
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ''
        maxP = ''
        for i in range(0,len(s)):
            for j in range(i,len(s)):
                if Solution.isPalindrome(s[i:j+1]):
                    maxP = s[i:j+1] if len(s[i:j+1])>len(maxP) else maxP
        return maxP