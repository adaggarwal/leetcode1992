'''
23. Merge k Sorted Lists

Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Example:

Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6

'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#STC - T O(nk (log k)) --> nk being the total elements; for each element there will be logk operation cost of insertion
# 			- S O(k(n+1)) --> nk elements list + k elements for the priority queue

class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        
        
        k = len(lists)
        heap = []
        start = dummy = ListNode(0)
        
        #initialize the PQ
        for i in range(0, k):
            if lists[i]:
                heap.append((lists[i].val, i))
                lists[i] = lists[i].next
        heapq.heapify(heap)

        #traverse through the lists while utilizing the size of heap as an exit paradigm
        while heap:
            #pop from the heap
            item = heapq.heappop(heap)
            #get the list number that was used to pick the smallest node
            listnumber = item[1]
            #add to the result list
            dummy.next = ListNode(item[0])
            #move forward in the result list
            dummy = dummy.next
            #fetch the new node
            nextNI = (listnumber)
            #push the next element if it exists otherwise we are skipping the empty list
            #meat: this is how the heap size will keep reducing and will ultimately tend to 0
            if lists[nextNI]:
                heapq.heappush(heap, (lists[nextNI].val,nextNI))
                #don't forget to push the individual list's pointer by one
                lists[nextNI] = lists[nextNI].next
                
        return start.next