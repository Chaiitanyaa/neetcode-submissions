class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        #append onto the regualr stack
        self.stack.append(val)
        
        #append onto the min stack based on what value is lower 
        if self.minStack == []:
            self.minStack.append(val)
        else:
            topElement = self.minStack[-1]
            self.minStack.append(min(topElement, val))
    

    def pop(self) -> None:
        
        self.minStack.pop()
        self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
