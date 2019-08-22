# 孩子兄弟表示法，可以以二叉树的形式表示多叉树
class CSTreeNode(object):
    def __init__(self, data):
        self.__data = data
        # left subtree
        self.first_child = None
        # right subtree
        self.right_sibling = None

    
from collections import deque

class CSTree(object):
    def __init__(self):
        self.__root = None

    def addNode(self, data):
        node = CSTreeNode(data)
        if self.__root == None:
            self.__root = node
        else:
            node_queue = deque()
            node_queue.append(self.__root)
            # level traverse by queue
            while node_queue:
                current_node = node_queue.popleft()
                if current_node.first_child == None:
                    current_node.first_child = node
                    return
                elif current_node.right_sibling == None:
                    current_node.right_sibling = node
                    return
                else:
                    node_queue.append(current_node.first_child)
                    node_queue.append(current_node.right_sibling)
