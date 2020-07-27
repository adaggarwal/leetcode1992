class Solution:
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack=[]
        path=[p for p in path.split('/') if p]
        for f in path:
            if f == '.': continue
            elif f == '..': 
                if stack: stack.pop()
            else: stack.append(f)
        return '/'+'/'.join(stack)
