# 二叉链表
class Node(object):
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None
    

class BinaryTree(object):
    def __init__(self):
        self.root = None

    # DFS: pre,mid,post order
    # recursive traverse
    def preorder_r(self, root):
        if root:
            print(root.data)
            self.preorder_r(root.left_child)
            self.preorder_r(root.right_child)

    def midorder_r(self, root):
        if root:
            self.preorder_r(root.left_child)
            print(root.data)
            self.preorder_r(root.right_child)

    def postorder_r(self, root):
        if root:
            self.preorder_r(root.left_child)
            self.preorder_r(root.right_child)
            print(root.data)

    # non-recursive traverse, by stack
    def preorder(self, root):
        node_stack = []
        if root:
            node_stack.append(root)
        while node_stack:
            current_node = node_stack.pop()
            print(current_node.data)
            if current_node.left_child:
                node_stack.append(current_node.left_child)
            if current_node.right_child:
                node_stack.append(current_node.right_child)
    
    def midorder(self, root):
        node_stack = []
        current_node = root
        while node_stack or current_node:
            # searching and push the left node to the stack contiously,
            # and the node is poped will be the root of every sub-tree
            if current_node:
                # root first in, so it will be poped out after left child
                node_stack.append(current_node)
                # the empty child node will be detected in the next while step
                current_node = current_node.left_child
            else:
                current_node = node_stack.pop()
                print(current_node.data)
                current_node = current_node.right_child

    def postorder(self, root):
        node_stack = []
        if root:
            node_stack.append(root)
        last_visited = None
        while node_stack:
            current_node = node_stack.pop()
            if current_node.left_child == None and current_node.right_child == None:
                print(current_node.data)
                last_visited = current_node
            # in post order traverse, 
            # if the right child is visited, then it is the last child,
            # if the left child is visited and there is no right child, then it is the last child as well 
            elif (last_visited == current_node.left_child and current_node.right_child == None) or last_visited == current_node.right_child:
                print(current_node.data)
                last_visited = current_node
            else:
                node_stack.append(current_node)
                # push right child before left child
                if current_node.right_child:
                    node_stack.append(current_node.right_child)
                if current_node.left_child:
                    node_stack.append(current_node.left_child)
    
    # by queue
    def level_traverse(self, root):
        from collections import deque
        node_queue = deque()
        if root:
            node_queue.append(root)
        while node_queue:
            current_node = node_queue.popleft()
            print(current_node.data)
            if current_node.left_child:
                node_queue.append(current_node.left_child)
            if current_node.right_child:
                node_queue.append(current_node.right_child)
