<<<<<<< HEAD
'''
20. Valid Parentheses

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true
Example 2:

Input: "()[]{}"
Output: true
Example 3:

Input: "(]"
Output: false
Example 4:

Input: "([)]"
Output: false
Example 5:

Input: "{[]}"
Output: true

'''

class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = list(s)
        par = {
                '(':')',
                '{':'}',
                '[':']'
        }
        result = []
        for elem in s:
            if elem in par.values():
                if len(result) and elem == par[result[-1]]:
                    result.pop()
                else:
                    return False
            else:
                result.append(elem)
        return True if len(result) == 0 else False
