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
        hashmap = {
            ')' : '(',
            ']' : '[',
            '}' : '{'
        }
        stack = []
        
        for el in s:
            if el not in hashmap:
                stack.append(el)
            else:
                if stack:
                    if hashmap[el] != stack.pop():
                        return False
                else:
                    return False
        return False if stack else True