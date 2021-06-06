class MinMaxStack:
    def __init__(self):
        self.stack = []
        self.minMaxStack = []

    def push(self, value):
        newMinMax = {"min": value, "max": value}

        if len(self.minMaxStack):
            newMinMax["min"] = min(self.minMaxStack[-1]["min"], value)
            newMinMax["max"] = max(self.minMaxStack[-1]["max"], value)

        self.stack.append(value)
        self.minMaxStack.append(newMinMax)

    def pop(self):
        if len(self.stack):
            self.stack.pop()
            self.minMaxStack.pop()
        else:
            print("Stack is empty")

    def peek(self):
        if len(self.stack):
            print(self.stack[-1])
        else:
            print("stack is empty")

    def min(self):
        if len(self.stack):
            print(self.minMaxStack[-1]["min"])
        else:
            print("stack is empty")

    def max(self):
        if len(self.stack):
            print(self.minMaxStack[-1]["max"])
        else:
            print("stack is empty")

    def printVal(self):
        print(self.stack)
        print(self.minMaxStack)


stack = MinMaxStack()
stack.push(5)
stack.push(3)
stack.min()
stack.push(7)
stack.peek()
stack.push(4)
stack.pop()
stack.peek()
stack.printVal()