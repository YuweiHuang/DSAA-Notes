# https: // blog.csdn.net/weixin_41958153/article/details/81258992
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or not head.next or not k:
            return head
        # 计算链表长度
        list_len = 0
        p = head
        while p:
            p = p.next
            list_len += 1
        # 快指针先走k步
        sp = fp = head
        k = k%list_len
        if k == 0:
            return head
        while k:
            fp = fp.next
            k -= 1
        
        # 同时遍历，快指针先到达尾部，慢指针的下一个节点就是移动k步之后的开头
        while fp.next:
            sp = sp.next
            fp = fp.next
        fp.next = head
        new_head = sp.next
        sp.next = None
        return new_head
