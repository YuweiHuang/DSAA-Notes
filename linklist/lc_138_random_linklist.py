# https://blog.csdn.net/qq_17550379/article/details/85775211
# https://wangxin1248.github.io/algorithm/2019/05/leetcode-138.html

"""
# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        # 复制next指针,在每个节点后面复制一个本身节点
        # 复制random指针
        # 恢复链表
        if not head:
            return None

        p = head
        while p:
            # 对节点的复制
            a = Node(p.val, p.next, None)
            p.next = a
            p = a.next
        # print('next')

        p = head
        while p:
            # 因为复制了新节点，所以random的next才是属于新链表的
            if p.random:
                p.next.random= p.random.next
            p = p.next.next
        # print('random')

        p = head
        new_head = p.next
        while p.next:
            tmp = p.next
            p.next = p.next.next
            p = tmp
        # print('recover')
        return new_head