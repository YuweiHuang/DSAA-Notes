# https://leetcode-cn.com/explore/learn/card/linked-list/194/two-pointer-technique/745/
# 解析： https://www.jianshu.com/p/c36e69e27d73

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # 0.额外空间的话，可以用map存储，第一个第二次访问的节点就是入口
        # 1.先找出快慢指针第一次相遇的点
        # 2.让慢指针和快指针以同样的速度，一个从head开始，一个从第一次相遇的点开始走
        # 3.第二次相遇，所指向的节点就是链表的环的入口
        fp = head
        sp = head
        while fp != None and sp != None and fp.next != None and sp.next != None:
            fp = fp.next
            if fp.next == None:
                return None
            fp = fp.next
            sp = sp.next
            if fp == sp:
                sp = head
                while fp != sp:
                    fp = fp.next
                    sp = sp.next
                return sp
        return None