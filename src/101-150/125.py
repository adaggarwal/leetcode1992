'''

125. Valid Palindrome

Share
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true
Example 2:

Input: "race a car"
Output: false

'''




class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = ''.join([el.lower() for el in s if el and el.isalnum()])
        start, end = 0, len(s)-1
        while start<end:
            if s[start] == s[end]:
                start += 1
                end -= 1
            else:
                return False
        return True