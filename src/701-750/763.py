'''
763. Partition Labels

A string S of lowercase letters is given. We want to partition this string into as many parts as possible so that each letter appears in at most one part, and return a list of integers representing the size of these parts.

Example 1:
Input: S = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.
Note:

S will have length in range [1, 500].
S will consist of lowercase letters ('a' to 'z') only.

'''
class Solution:
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        dictionary = {}
        for ind,el in enumerate(S):
            dictionary[el] = ind
        anchor, current, end, retL = 0, 0, 0, []
        while current < len(S):
            if S[current] in dictionary:
                end = max(end,dictionary[S[current]])
                del dictionary[S[current]]
            if current == end:
                retL.append((end-anchor) + 1)
                anchor = current + 1
            current += 1 
        return retL