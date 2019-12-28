'''
Traverse the linked-list and simultaneously create nodes with value equal to sum of current nodes' values 
While adding the values, carry needs to be stored in case its generated and reset otherwise
Edge cases where one list ends prematurely could be very common. To handle that - default to 0 value so it doesnt change the sum value.
Carry can also retain an overflow value which simply means an extra node needs to be added to the current resultant list.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        returnVal = dummy = ListNode(None)
        carry = 0
        if not l1:
            return l2
        if not l2:
            return l1
        while l1 or l2:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            sumVal = v1 + v2 + carry 
            print(sumVal)
            if sumVal > 9:
                carry = 1
                sumVal = sumVal%10
            else:
                carry = 0
            temp = ListNode(sumVal)
            dummy.next = temp
            dummy = temp
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        if carry:
            dummy.next = ListNode(carry)
        return returnVal.next