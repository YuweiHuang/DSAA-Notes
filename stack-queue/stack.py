class Stack(object):
    def __init__(self, size):
        self.__top = -1
        self.__size = size
        self.__data = [None for i in range(self.__size)]

    def isFull(self):
        return self.__top == self.__size-1

    def isEmpty(self):
        return self.__top == -1

    def getTop(self):
        return self.__data[self.__top]

    # return the state of push stack
    def push(self, data):
        if self.isFull():
            raise "stack is full"
        else:
            self.__top += 1
            self.__data[self.__top] = data

    def pop(self, data):
        # stack is empty
        if self.isEmpty():
            raise "stack is empty"
        else:
            x = self.getTop()
            self.__top -= 1
            return x

    def clearStack(self):
        if self.isEmpty():
            raise "stack is empty"
        else:
            self.__top = -1

    def totalElements(self):
        return self.__top + 1