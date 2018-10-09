'''
206. Reverse Linked List

Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
Follow up:

A linked list can be reversed either iteratively or recursively. Could you implement both?
'''

# recursive solution:
class Solution:
    def reverseList(self, head):
        return self.reverse(head)

    def reverse(self, node, prev=None):
        if node == None:
            #meat: return the previous node when the control reaches the end of the recursion traversal
            # as the prev is supposed to have the starting reference to the reversed list
            return prev
        nextNode = node.next
        node.next = prev
        return self.reverse(nextNode, node)


# iterative solution
class Solution:
    def reverseList(self, head):
        prev = None
        while head:
            nNode = head.next
            head.next = prev
            prev = head
            head = nNode
        return prev