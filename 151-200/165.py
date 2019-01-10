'''
165. Compare Version Numbers
Medium
204
925


Compare two version numbers version1 and version2.
If version1 > version2 return 1; if version1 < version2 return -1;otherwise return 0.

You may assume that the version strings are non-empty and contain only digits and the . character.
The . character does not represent a decimal point and is used to separate number sequences.
For instance, 2.5 is not "two and a half" or "half way to version three", it is the fifth second-level revision of the second first-level revision.

Example 1:

Input: version1 = "0.1", version2 = "1.1"
Output: -1
Example 2:

Input: version1 = "1.0.1", version2 = "1"
Output: 1
Example 3:

Input: version1 = "7.5.2.4", version2 = "7.5.3"
Output: -1
'''
'''
Runtime O(max(version1,version2))

Approach
1. append dummy Zeroes to the smaller version to make the comparison easier
2. compare each integeral value delimited by '.', as soon as either is bigger than the other, return the pertinent value (1/-1)
3. if nothing was returned, then both the versions were same

For more checkout - https://github.com/adityaaggarwal1992/leetcode1992

'''

class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        
        version1 = version1.split(".")
        version2 = version2.split(".")
        
        diff = len(version1) - len(version2)
        
        if diff > 0:
            while diff:
                version2.append("0")
                diff -= 1
        elif diff < 0:
            diff = abs(diff)
            while diff:
                version1.append("0")
                diff -= 1
                
        for i in range(0, len(version1)):
            if int(version1[i])< int(version2[i]):
                return -1
            if int(version1[i])> int(version2[i]):
                return 1            
                
        return 0 