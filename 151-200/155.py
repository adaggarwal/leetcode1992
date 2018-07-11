Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.


Example:
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> Returns -3.
minStack.pop();
minStack.top();      --> Returns 0.
minStack.getMin();   --> Returns -2.

'''
Use a tuple to store minimum and the value
each couple will be like - (value, minimum in the stack till this value)
'''

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stk = list()

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if len(self.stk) == 0:
            self.stk.append((x,x))
        else:
            minim = self.getMin()
            self.stk.append((x,min(x,minim)))

    def pop(self):
        """
        :rtype: void
        """
        if len(self.stk) == 0:
            raise ValueError("Empty stack Exception!")
        else:
            self.stk.pop()

    def top(self):
        """
        :rtype: int
        """
        if len(self.stk) == 0:
            raise ValueError("Empty stack Exception")
        else:
            val, dc= self.stk[-1]
            return val
        

    def getMin(self):
        """
        :rtype: int
        """
        if len(self.stk) == 0:
            raise ValueError("Empty stack Exception")
        else:
            dc,minim = self.stk[-1]
            return minim

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
