'''
224. Basic Calculator

Implement a basic calculator to evaluate a simple expression string.

The expression string may contain open ( and closing parentheses ), the plus + or minus sign -, non-negative integers and empty spaces .

Example 1:

Input: "1 + 1"
Output: 2
Example 2:

Input: " 2-1 + 2 "
Output: 3
Example 3:

Input: "(1+(4+5+2)-3)+(6+8)"
Output: 23
Note:
You may assume that the given expression is always valid.
'''

class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        result, operator, currentNumber, stack = 0, 1, 0, list()
        for character in s:
            if character == ' ':
                continue
            elif character.isdigit():
                #number can be multi-digit
                currentNumber = currentNumber*10 + int(character)
            elif character == '(':
                #put the current result in the stack alongwith the operator behind '('
                #first push the result
                stack.append(result)
                stack.append(operator)
                #reset the operator and results
                operator, result = 1, 0
            elif character == '+':
                #operator encountered; a currentNumber is definitely expected before this encounter
                result += operator*currentNumber
                #currentNumber is used, reset it
                currentNumber = 0
                #update the operator
                operator = 1
            elif character == '-':
                result += operator*currentNumber
                currentNumber, operator = 0, -1
            elif character == ')':
                result += currentNumber*operator
                #now the result acts as currentNumber -->  || XYZ - (result) || So the result absorbs the polarity of operatory as below:
                result *= stack.pop()
                #now the older result can be popped and combined with currentNumber aliased as results
                result += stack.pop()
                #reset the currentNumber
                currentNumber = 0

        #consider a case like 1+1; the last digit will be initialized in currentNumber; but wouldn't be handled; hence:
        if currentNumber:
            result += currentNumber*operator
        return result
