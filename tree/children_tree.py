# 孩子表示法
class ChildrenTreeNode(object):
    # linklist, to reprensent the relation among parents and children
    def __init__(self, child=None, next_child=None):
        self.__child = child
        self.__next_child = next_child

class ChildrenTreeBox(object):
    #the head list of children linklist
    def __init__(self, data, firstchild):
        self.__data = data
        self.__firstchild = ChildrenTreeNode()

class ChildrenTree(object):
    def __init__(self, size):
        self.__size = size
        self.__tree_data = []
        self.__root_index = 0

    




