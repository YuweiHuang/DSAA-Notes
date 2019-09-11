# https://github.com/cy69855522/Shortest-LeetCode-Python-Solutions
"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

from collections import deque
class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        stack = deque()
        if head:
            stack.append(head)

        p = None
        while stack:
            node = stack.pop()
            if node.next:
                stack.append(node.next)
            if node.child:
                stack.append(node.child)
            if p:
                p.next = node
                node.prev = p

                p.child = node.child = None
            p = node
        return head
