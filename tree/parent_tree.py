# 双亲表示法
class ParentTreeNode(object):
    def __init__(self, data, parent):
        self.__data = data
        self.__parent = parent

class ParentTree(object):
    def __init__(self, size):
        # the number of nodes
        self.__size = size
        self.__tree_data = []
        self.__root_index = 0

    def addNode(self, data, parent):
        node = ParentTreeNode(data, parent)
        if parent == -1:
            if not self.__tree_data:
                self.__tree_data.append(node)
            else:
                raise Exception('root exists')
        
        else:
            self.__tree_data.append(node)

    # time complexity: O(1)
    def getParent(self, index):
        return self.__tree_data[self.__tree_data[index].parent]

    # high time complexity, this func may search the whole tree: O(n)
    def getChildren(self, index):
        children = []
        for node in self.__tree_data:
            node.parent == index
            children.append(node)
        return children
