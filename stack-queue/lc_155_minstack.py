class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = []
        self.min_index = -1
        self.min_index_stack = []
        self.cur_index = -1
        # print()

    def push(self, x: int) -> None:
        
        if self.data == []:
            self.data.append(x)
            self.min_index = 0
            self.cur_index = 0
        else:
            self.data.append(x)
            self.cur_index += 1
            # == will affect the pop operation
            if x <= self.data[self.min_index_stack[-1]]:
                self.min_index = self.cur_index

        self.min_index_stack.append(self.min_index)        
        # print('push: ', self.min_index_stack)
        # print(self.data)

    def pop(self) -> None:
        self.min_index_stack.pop()
        self.data.pop()
        self.cur_index -= 1
        if self.min_index_stack != []:
            self.min_index = self.min_index_stack[-1]
        # print('pop: ', self.min_index_stack)
        # print(self.data)

    def top(self) -> int:
        return self.data[-1]

    def getMin(self) -> int:
        return self.data[self.min_index]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()