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
Return the longest palindrome

Time - O(n^3)
Space - O(1) // O(n) if return string is counted (open to debate) 
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


'''
Mod - Dynamic Programming Soln

For each element -- try to expand around that element assuming it to be the center of our prospective palindrome!!
For most elements this would fail which is good as it provides great speedup there, GREAT :)

For elements which are palindromes around the center -- return the length of the palindrome and record the START and END in case this length is more than the ones seen before

?? Why do we call getLength two times?
-- Well we do that because this prospective palindrome could might as well be an even one or an odd one, think of an example like -- "ROSOR" this is an odd length palindrome. Now, 
if we expand around 'S' we do get an answer. But if we expand 'O' and 'S', we won't get any answers here, a length of 0 will be returned.
So, a simple solution would be to assume any given position can be the center of either an even or an odd palindrome -> then use the bigger value. Let me ask a question, each time 
if its an even palindrome, what would be the cost of calling the getLength function with odd palindrome arguments? Well it will be 0. And max(0,'>0 value') will be '>0'. Hence,
we don't loose any time here. 

Time - O(n^2)
Space - O(1) // O(n) in case return val is considered
'''

class Solution:
    
    @staticmethod
    def getLength(s, left, right):
        while (left>=0) and (right<len(s)) and (s[left]==s[right]):
            right += 1
            left -= 1
        return right-left-1
    
    def longestPalindrome(self, s: str) -> str:
        if (not s) or len(s)<2:
            return s
        START = END = 0
        for i in range(len(s)):
            #oddPalindromic sequences
            lengthOddP = self.getLength(s, i, i)
            #evenPalindromic sequences
            lengthEvenP = self.getLength(s, i, i+1)
            actualLen = max(lengthEvenP, lengthOddP)
            if (END - START + 1) < actualLen:
                END = i + actualLen//2
                START = i - (actualLen-1)//2
        return s[START:END+1]