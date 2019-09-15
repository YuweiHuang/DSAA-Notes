class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self._size = size + 1
        self._front = 0
        self._rear = 0
        self._data = [None for i in range(self._size)]
        self._total = 0
        self._num = 0
    
    def _isFull(self):
        return (self._rear + 1) % self._size == self._front

    def next(self, val: int) -> float:
        if self._isFull():
            self._num -= 1
            self._total -= self._data[self._front]
            self._front = (self._front + 1) % self._size
        
        self._num += 1
        self._data[self._rear] = val
        self._rear = (self._rear + 1) % self._size
        self._total = self._total + val
        return self._total / self._num
        