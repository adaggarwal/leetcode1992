'''

138. Copy List with Random Pointer


A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

Return a deep copy of the list.
'''


# 1.Recursive STC - [O(n), O(n)]

# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None



class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        #initialize a dictionary to keep a track of visited nodes
        self.hashmap = {}
        
        #call another function to return the copy of deep list
        node = self.returnDeepList(head)
        
        return node
    
    def returnDeepList(self, head):
        '''
        :type head: RandomListNode
        :rtype: RandomListNode
        '''
        
        if head == None:
            return head
        
        #head is not null now, let's check if the head already exists in the object's hash
        if head in self.hashmap:
            return self.hashmap[head]
        
        #head is not null and is a new node
        newNode = RandomListNode(head.label)
        #add this to the visited nodes too
        self.hashmap[head] = newNode
        
        #lets determine the two recursive branches now
        newNode.next = self.returnDeepList(head.next)
        newNode.random = self.returnDeepList(head.random)
        
        return newNode



##################################

#2. Iterative STC = O(1), O(n)

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if head == None:
            return head
        
        headclone = head
        
        #pass 1: tweak the list such that the list doubles and a clone element appears next to each element
        while headclone:
            node = RandomListNode(headclone.label)
            node.next = headclone.next
            headclone.next = node
            headclone = node.next
            
        newNode = head.next
        #pass 2: copy the random refrences from original to the clones
        headclone = head
        while headclone:
            headclone.next.random = headclone.random.next if headclone.random else None
            headclone = headclone.next.next
        
        #pass3: detangle the clone list
        headclone = head

        while headclone:
            if headclone.next.next:
                temp = headclone.next.next
                headclone.next.next = headclone.next.next.next
            else:
                temp = None
                headclone.next.next = None
            headclone.next = temp
            headclone = headclone.next
            
        return newNode
