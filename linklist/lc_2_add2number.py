# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        p1 = l1
        p2 = l2
        l3 = ListNode(None)
        p3 = l3
        tmp = 0
        v = 0
        while p1 or p2:
            if p1 and p2:
                v = p1.val + p2.val + tmp
                p1 = p1.next
                p2 = p2.next
            elif p1 and not p2:
                v = p1.val + tmp
                p1 = p1.next
            else:
                v = p2.val + tmp
                p2 = p2.next
            tmp = int(v/10)
            p3.next = ListNode(v%10)
            p3 = p3.next
        if tmp:
            p3.next = ListNode(tmp)
        else:
            p3.next = None
        return l3.next
