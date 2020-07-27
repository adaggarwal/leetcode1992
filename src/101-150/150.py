'''
1. lets create a dictionary hashmap of what needs to happen when an operator is encountered. 
2. traverse through the tokens and catch all the numbers preceeding the operator. 
3. pop the last two numbers -> perform the operation and store it in the stack.
4. keep repeating 2 and 3 
5. you'll ultimately be left with the result in the stack
'''

class Solution:
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        if len(tokens) < 1:
            return None
        ops = {
            '+' : lambda y, x: x+y,
            '-' : lambda y, x: x-y,
            '*' : lambda y, x: x*y,
            '/' : lambda y, x: int(x/y)
        }
        result = []
        for token in tokens:
            if token in ops.keys():
                result.append(ops[token](result.pop(), result.pop()))
            else:
                result.append(int(token))
        return result[0]
