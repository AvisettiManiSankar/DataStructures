from collections import deque
import time
import threading

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
orders = ['pizza','samosa','pasta','biryani','burger']

def PlaceOrder():
    while orders:
        order = orders.pop(0)
        queue.enqueue(order)
        print(f"Order Placed : {order}")
        time.sleep(0.5)

def ServeOrder():
    while not queue.is_empty():
        order = queue.dequeue()
        print(f"Order Served: {order}")
        time.sleep(2)

product_thread = threading.Thread(target=PlaceOrder)
serve_thread = threading.Thread(target=ServeOrder)

print("Place Order thread started.")
product_thread.start()

time.sleep(1)

print("Serve Order thread started.")
serve_thread.start()

product_thread.join()
serve_thread.join()

print("Food ordering system has been shut down.")