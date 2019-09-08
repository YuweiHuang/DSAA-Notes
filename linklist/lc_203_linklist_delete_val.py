# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if not head:
            return head
        # 空节点作为头结点
        h = ListNode(None)
        h.next = head
        pre = h
        cur = h.next
        while h.next and cur:
            if cur.val == val:
                pre.next = cur.next
                # pre 不变
            else:
                # pre 要变
                pre = cur
            cur = cur.next
        return h.next
