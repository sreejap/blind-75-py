# T(C) -  the expensive while self.in_stack: work doesn’t happen every time—it happens only when out_stack is empty, 
# and each element can be moved from in_stack to out_stack only once per push. Over a long sequence of operations, the total work “spreads out,” giving amortized 
# O (1), O(1) per operation.
class MyQueue:

    def __init__(self):
        self.in_stack = []
        self.out_stack = []        

    def push(self, x: int) -> None:
        self.in_stack.append(x)        

    def populate_out_stack(self): # we need to pass the self
        if not self.out_stack:
            while self.in_stack: 
                self.out_stack.append(self.in_stack.pop()) 

    def pop(self) -> int:
        self.populate_out_stack()
        return self.out_stack.pop()

    def peek(self) -> int:
        self.populate_out_stack()
        return self.out_stack[-1]

    def empty(self) -> bool:
        return len(self.in_stack) == 0 and len(self.out_stack) == 0

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
