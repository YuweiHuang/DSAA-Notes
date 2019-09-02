# https: // leetcode-cn.com/explore/learn/card/linked-list/193/singly-linked-list/741/
class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = Node(None)        

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        cnt = 0
        cur_node = self.head.next
        while cur_node != None:
            if cnt == index:
                return cur_node.data
            cur_node = cur_node.next
            cnt += 1
        return -1
        
    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        new_node = Node(val)
        new_node.next = self.head.next
        self.head.next = new_node
        
    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        new_node = Node(val)
        cur_node = self.head
        while cur_node.next != None:
            cur_node = cur_node.next
        cur_node.next = new_node
        
    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        new_node = Node(val)
        if index < 0:
            new_node.next = self.head.next
            self.head.next = new_node
        else:
            cnt = 0
            pre_node = self.head
            cur_node = self.head.next
            while cur_node != None:
                if cnt == index:
                    new_node.next = cur_node
                    pre_node.next = new_node
                pre_node = cur_node
                cur_node = cur_node.next
                cnt += 1
            if cnt == index:
                pre_node.next = new_node

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index >= 0:
            cur_node = self.head.next
            pre_node = self.head
            cnt = 0
            while cur_node != None:
                if cnt == index:
                    pre_node.next = cur_node.next
                    cur_node = None
                    break
                else:
                    pre_node = cur_node
                    cur_node = cur_node.next
                    cnt += 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# obj.addAtHead(1)
# print(obj.get(0))
# print(obj.get(1))
# obj.addAtIndex(1,2)
# print(obj.get(1))
# print(obj.get(0))
# print(obj.get(2))
# obj.deleteAtIndex(1)
# print(obj.get(1))
