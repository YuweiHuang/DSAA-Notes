# 解析：https://blog.csdn.net/songyunli1111/article/details/79416684
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # 0.将原链表上的元素移动到新链表上
        # 1.判断边界
        # 2.注意保存原链表中头结点的下一个结点，免得丢失链表
        if not head or not head.next:
            return head
        new_head = None
        while head:
            # 保存下一结点，以免丢失
            tmp = head.next
            # 更换到新的链表上
            head.next = new_head
            # 更换新链表的头结点
            new_head = head
            # 更换原链表头结点
            head = tmp
        return new_head

            
