

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
