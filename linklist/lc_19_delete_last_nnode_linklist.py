# https://blog.csdn.net/qq_17550379/article/details/80717212
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        # 双指针法
        # 0.注意head不是第一个元素，是一个空节点，结构：head->1->2->3->None
        # 1.让快指针先走N步骤
        # 2.快慢指针同时走
        # 3.快指针到达尾部的时候，慢指针指向的下一个就是要删除的节点
        h = ListNode(-1)
        h.next = head
        fp = h
        sp = h
        for _ in range(n):
            fp = fp.next
        while fp and fp.next:
            fp = fp.next
            sp = sp.next
        sp.next = sp.next.next
        return h.next
