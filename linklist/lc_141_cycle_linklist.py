# https: // leetcode-cn.com/explore/learn/card/linked-list/194/two-pointer-technique/744/
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
        # 1.将快慢指针指向头节点，快指针速度是慢指针的两倍
        # 2.当快慢指针相遇的时候就说明链表有环，并且环的长度等于步数
        fp = head
        sp = head
        while fp != None and sp != None and fp.next != None and sp.next != None:
            fp = fp.next
            if fp.next == None:
                return False
            else:
                fp = fp.next
            sp = sp.next
            if fp == sp:
                return True
        return False
            
        
