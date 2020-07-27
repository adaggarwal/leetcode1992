'''
253. Meeting Rooms II
Medium
908
16
Favorite
Share
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.

Example 1:

Input: [[0, 30],[5, 10],[15, 20]]
Output: 2
Example 2:

Input: [[7,10],[2,4]]
Output: 1

'''

'''

Approach

1. Let's take an approach which uses sorting and usage of heap [O(nlogn)]
2. Simply start with sorting the interval object by the start time. Reason -> Get a mapping of what meetings would start earlier than others
3. Utilizing the stack we push the end time of first meeting in the heap. Simultaneously, we end up using one room. 
4. As we move on to the next meetings and so on so forth, just peek the smallest element in the heap. This is the time when the room(that will tend to get freed up 
faster than others) will be freed up. If current meeting's start time is more than or equal to the last end time in the stack; we can safely use this room rather than 
getting a new room. As we are utilizing this room, push the current end time and pop the smallest end time at the respective interval. This is important as we intend to 
re-use this room.
5. Similarly, as we come across cases wherein the end time is lesser than the last end time in the stack. We simple allocate this meeting a new room and push the meeting's end 
time onto the stack so that it can be reused later. 

For solutions to other problems, visit -> https://github.com/adityaaggarwal1992/leetcode1992

'''

# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        result = 0
        intervals.sort(key = lambda x: x.start)
        heap = []
        heapq.heapify(heap)
        for element in intervals:
            if heap and heap[0] <= element.start:
                heapq.heappushpop(heap, element.end)
            else:
                result += 1
                heapq.heappush(heap, element.end)  
        return result