# https: // blog.csdn.net/qq_34364995/article/details/80640449
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):

    def reverse_linlist(self, head):
        if not head or not head.next:
            return head
        new_head = None
        while head:
            tmp = head.next
            head.next = new_head
            new_head = head
            head = tmp
        return new_head

    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # 0.快慢指针
        # 1.快指针走到尾部的时候，慢指针刚好走到中点
        # 2.反转链表后半段(慢指针后面)
        # 3.从头开始比较元素是否相同

        # 0个或1个元素

        if not head or not head.next:
            return True
        # 2个元素
        # 1->2->1
        if not head.next.next:
            return head.val == head.next.val
        fp = head
        sp = head
        while fp.next and fp.next.next:
            sp = sp.next
            fp = fp.next.next
        l = head
        r = self.reverse_linlist(sp.next)
        while r.next:
            if l.val == r.val:
                l= l.next
                r = r.next
            else:
                return False
        return l.val == r.val
