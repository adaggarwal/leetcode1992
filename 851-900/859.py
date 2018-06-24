#Given two strings A and B of lowercase letters, return true if and only if we can swap two letters in A so that the result equals B.
#
# 
#
#Example 1:
#
#Input: A = "ab", B = "ba"
#Output: true
#Example 2:
#
#Input: A = "ab", B = "ab"
#Output: false
#Example 3:
#
#Input: A = "aa", B = "aa"
#Output: true
#Example 4:
#
#Input: A = "aaaaaaabc", B = "aaaaaaacb"
#Output: true
#Example 5:
#
#Input: A = "", B = "aa"
#Output: false
# 
#
#Note:
#
#0 <= A.length <= 20000
#0 <= B.length <= 20000
#A and B consist only of lowercase letters.

'''
Lets start with eliminating false corner cases like
1. Length of A not equals to B
2. if 1. is true then length of both A and B is equal; now lets check when length of both of them is 1 and if A == B or not
3. if 1 and 2 are true; lets check if all the elements in A are present in B
4. Create an empty set, a variable to count the conflicts and another to flag if there are repetitions
5. compare each item in both the strings consecutively; if its equal save it in the set if its already not there. Incase, its there increase the flag's value to hint that there were duplicates -> that too on the same places. Remember cases like -> A = aa and B = aa are true
6. in the end if we have count's value 2 or if count is 0 but there are repetitive duplicates; our answer is true otherwise false
'''

class Solution(object):
    def buddyStrings(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        count, rep = 0, 0
        if len(A) != len(B) or (len(A) == 1 and A != B) or sorted(A) != sorted(B):
            return False
        EqualElements = set()
        for (X,Y) in zip(A,B):
            if X == Y:
                if X in EqualElements:
                    rep += 1
                else:
                    EqualElements.add(X)
            else:
                count += 1
        return True if count == 2 or (count == 0 and rep) else False
