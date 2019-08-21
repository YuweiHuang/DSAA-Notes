class Queue(object):
    def __init__(self, size):
        self.__size = size
        # point to the first element in the queue
        self.__front = 0
        # point to the next position after the last element in the queue
        self.__rear = 0
        self.__data = [None for i in range(self.__size)]

    def isFull(self):
        # left on empty position to help queue full judgement
        # total elements the queue can store is size -1
        return (self.__rear + 1) % self.__size == self.__front

    def isEmpty(self):
        return self.__front == self.__rear

    def clearQueue(self):
        self.__front = 0
        self.__rear = 0

    def getHead(self):
        if self.isEmpty():
            raise Exception('queue is empty')
        else:
            return self.__data[self.__front % self.__size]

    def enqueue(self, data):
        if self.isFull():
            raise Exception('queue is full')
        else:
            self.__data[self.__rear] = data
            self.__rear = (self.__rear + 1) % self.__size
 
    def dequeue(self):
        if self.isEmpty():
            raise Exception('queue is empty')
        else:
            x = self.__data[self.__front]
            self.__front = (self.__front + 1) % self.__size

    def queueLength(self):
        return (self.__rear + self.__size - self.__front) % self.__size

    