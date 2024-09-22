from collections import deque

class Queue:
    def __init__(self):
        self.queue = deque()
    
    def enqueue(self, item):
        self.queue.appendleft(item)

    def dequeue(self):
        if len(self.queue) ==0:
            print("Queue is empty")
            return
        return self.queue.pop()

    def peek(self):
        return self.queue[-1]
    
    def size(self):
        return len(self.queue)
    
    def is_empty(self):
        return len(self.queue) == 0
    
queue = Queue()

def generate_binary(number):
    queue.enqueue("1")
    for i in range(number):
        print(f"Binary Number for {i+1}: {queue.peek()}")
        queue.enqueue(queue.peek()+"0")
        queue.enqueue(queue.peek()+"1")
        queue.dequeue()

generate_binary(100)
