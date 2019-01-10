'''
17. Letter Combinations of a Phone Number
Medium

1702

242

Favorite

Share
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

Example:

Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
'''

class Solution:
    # @param {string} digits
    # @return {string[]}
    def letterCombinations(self, digits):
        
        if not digits:
            return []
        
        mapping = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', 
                   '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        
        if len(digits) == 1:
            return list(mapping[digits[0]])
        
        result = []
        front = mapping[digits[0]]
        end = self.letterCombinations(digits[1:])
        for element in front:
            for char in end:
                result.append(element + char)
        return result