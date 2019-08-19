class Node(object):
    def __init__(self, data):
        self.__data = data
        self.__next = None
        self.__previous = None

    def getData(self):
        return self.__data

    def setData(self, new_data):
        self.__data = new_data

    def getPrevious(self):
        return self.__previous

    def setPrevious(self, new_previous):
        self.__previous = new_previous

    def getNext(self):
        return self.__next

    def setNext(self, new_next):
        self.__next = new_next


class DoubleLinkList(object):
    def __init__(self):
        self.head = Node(None)
        self.tail = Node(None)
        self.head.setNext(self.tail)
        self.tail.setPrevious(self.head)

    def addNode(self, data):
        new_node = Node(data)
        new_node.setNext(self.tail)
        new_node.setPrevious(self.head)
        self.head.setNext(new_node)
        self.tail.setPrevious(new_node)
    
    def isInList(self, data):
        current_node = self.head.getNext
        while current_node != self.tail:
            if current_node.getData() == data:
                return True
            current_node = current_node.getNext()
        return False

    def deleteNode(self, data):
        current_node = self.head.getNext()
        while current_node != self.tail:
            if current_node.getData() == data:
                previous_node = current_node.getPrevious()
                previous_node.setNext(current_node.getNext())
                current_node.getNext().setPrevious(previous_node)

                current_node.setData(None)
                current_node.setNext(None)
                current_node.setPrevious(None)
                return True

        return False

    def getSize(self):
        size = 0
        current_node = self.head.getNext
        while current_node != self.tail:
            size += 1
            current_node = current_node.getNext()
        return size
