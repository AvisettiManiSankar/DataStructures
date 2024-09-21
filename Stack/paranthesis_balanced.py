from collections import deque

class Stack:
    def __init__(self):
        self.stack = deque()

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop()
    
    def peek(self):
        return self.stack[-1]
    
    def is_empty(self):
        return len(self.stack) == 0
    
    def size(self):
        return len(self.stack)


def is_balanced(expression):
    stack = Stack()

    pairs = {')':'(', '}':'{', ']':'['}

    for char in expression:
        if char in '{([':
            stack.push(char)
        elif char in '})]':
            if stack.is_empty() or stack.pop() != pairs[char]:
                return False
    return stack.is_empty() == 0

expression = '[(]'

if is_balanced(expression):
    print(f"The expression '{expression}' is balanced.")
else:
    print(f"The expression '{expression}' is not balanced.")