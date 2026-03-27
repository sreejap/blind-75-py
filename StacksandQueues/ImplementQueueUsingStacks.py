# T(C) -  the expensive while self.in_stack: work doesn’t happen every time—it happens only when out_stack is empty, 
# and each element can be moved from in_stack to out_stack only once per push. Over a long sequence of operations, the total work “spreads out,” giving amortized 
# O (1), O(1) per operation.
# More notes:
# Yes—populate_out_stack must take self here, because it’s an instance method that reads/writes instance attributes (self.in_stack, self.out_stack) and is called as self.populate_out_stack() from other instance methods.

# What self does in your snippet
# When you do:

# self.populate_out_stack()
# Python translates that roughly to:

# MyQueue.populate_out_stack(self)
# So the instance (self) is automatically passed in, and inside populate_out_stack you can access:

# self.out_stack
# self.in_stack
# If you removed self from the definition
# If you wrote:

# def populate_out_stack():
#     ...
# then calling self.populate_out_stack() would raise a TypeError because Python would still pass the instance automatically, but the function wouldn’t accept it.

# Your code is correct as written
# This is the standard “queue using two stacks” implementation, and populate_out_stack is correctly an instance method.

# (Only if populate_out_stack didn’t use any instance state would @staticmethod make sense—but here it does, so keep self.)


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
