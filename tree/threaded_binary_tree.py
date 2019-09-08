
class Node(object):
    def __init__(self, data):
        self.lchild = None
        self.rchild = None
        self.ltag = None
        self.rtag = None
        self.data = data

class ThreadedBinaryTree(object):
    def __init__(self):
        self.root = None

    def midorder_thred(self, root):
        if root:
            self.midorder_thred(root.lchild)
            self.add_thread(root)
            self.midorder_thred(root.rchild)