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
        if root == None:
            return
        else:
            print(root.data)
            self.preorder_r(root.left_child)
            self.preorder_r(root.right_child)

    def midorder_r(self, root):
        if root == None:
            return
        else:
            self.preorder_r(root.left_child)
            print(root.data)
            self.preorder_r(root.right_child)

    def postorder_r(self, root):
        if root == None:
            return
        else:
            self.preorder_r(root.left_child)
            self.preorder_r(root.right_child)
            print(root.data)

    # non-recursive traverse, by stack
    def preorder(self, root):
        node_stack = []
        current_node = root
        if current_node != None:
            node_stack.append(current_node)
        while node_stack != []:
            current_node = node_stack.pop()
            print(current_node.data)
            if current_node.left_child != None:
                node_stack.append(current_node.left_child)
            if current_node.right_child != None:
                node_stack.append(current_node.right_child)
    
    def midorder(self, root):
        node_stack = []
        current_node = root
        while node_stack != [] or current_node != None:
            # searching and push the left node to the stack contiously, 
            # and the node is poped will be the root of every sub-tree
            if current_node != None:
                node_stack.append(current_node)
                # the empty child node will be detected in the next while step
                current_node = current_node.left_child
            else:
                current_node = node_stack.pop()
                print(current_node.data)
                current_node = current_node.right_child


    def postorder(self, root):
        pass

    
    # by queue
    def level_traverse(self, root):
        pass

    