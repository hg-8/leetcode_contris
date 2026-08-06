class MinStack:

    def __init__(self):
        self.a=[]
        self.b=[]
    def push(self, value: int) -> None:
        self.a.append(value)
        if (len(self.b) == 0 or value <= self.b[-1]):
            self.b.append(value)

    def pop(self) -> None:
        if len(self.a)>0 and len(self.b)>0:
            if self.a[-1] == self.b[-1]:
                self.b.pop()
            self.a.pop()


    def top(self) -> int:
        return self.a[-1]

    def getMin(self) -> int:
        return self.b[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()