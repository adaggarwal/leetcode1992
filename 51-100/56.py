'''
56. Merge intervals

1. sort the given list of objects based on starting point of each interval object.  O(nlogn)

2. use another list and append items from the sorted list of objects. just remember to do a simple check before each insertion.  O(n)

    2.1 Everytime you insert, first check if the last object which is already present's end should be lesser than the current object to be inserted's start. If its less, insert the new object
    2.2 if it is larger or equal then, change the last object in the output list in a way that it's end is the max(its own end value, iterative object's end value) O(1)

Overall -> O(nlogn)
'''

# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        intervals = sorted(intervals, key = lambda interval: interval.start)
        out = []
        for interval in intervals:
            if out:
                if out[-1].end >= interval.start:
                    out[-1].end = max(out[-1].end, interval.end)
                else:
                    out.append(interval)
            else:
                out.append(interval)
        return out
