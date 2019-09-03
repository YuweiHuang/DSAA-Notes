# https://blog.csdn.net/qq_34840129/article/details/81098528
# https://leetcode-cn.com/explore/learn/card/linked-list/194/two-pointer-technique/746/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        # 1.先同时遍历两条链表，如果到终止的时候发现尾节点相同，则说明有交汇点，记下此时的步数差d
        # 2.先让长的链表遍历d步再同时开始遍历，两条链表上的节点第一次相遇就是两链表的交汇点
        # 3.注意边界：空链表，一个元素链表
        lp = headA
        rp = headB
        left_len = 0
        right_len = 0
        if headA == None or headB == None:
            return None
        while headA != None and lp.next != None:
            lp = lp.next
            left_len += 1
        while headB != None and rp.next != None:
            rp = rp.next
            right_len += 1
        if lp == rp:
            lp = headA
            rp = headB
            d = left_len - right_len
            if d < 0:
                d = -d
                for i in range(d):
                    rp = rp.next
            else:
                for i in range(d):
                    lp = lp.next
            while lp != rp:
                lp = lp.next
                rp = rp.next
            return lp
        else:
            return None

