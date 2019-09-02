# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        fp = head
        lp = head
        while fp != None and lp != None and fp.next != None and lp.next != None:
            fp = fp.next
            if fp.next == None:
                return False
            else:
                fp = fp.next
            lp = lp.next
            if fp == lp:
                return True
        return False
            
        