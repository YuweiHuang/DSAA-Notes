# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        p1 = l1
        p2 = l2
        l3 = ListNode(None)
        p3 = l3
        
        while p1 and p2:
            if p1.val <= p2.val:
                p3.next = p1
                p1 = p1.next
            else:
                p3.next = p2
                p2 = p2.next
            p3 = p3.next

        # p1 is not empty and p2 is empty
        if p1 and not p2:
            p3.next = p1
        elif not p1 and p2:
            p3.next = p2
        else:
            p3.next = None
        return l3.next
        

        
