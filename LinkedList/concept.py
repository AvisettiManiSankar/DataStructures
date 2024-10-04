class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_begining(self, data):
        self.head = Node(data,self.head)

    def insert_at_end(self,data):
        node = Node(data, None)
        if(self.head is None):
            self.head = node
            return
        next_node = self.head
        while next_node.next:
            next_node = next_node.next
        next_node.next = node

    def insert_values(self, data_list):
        self.head = None
        for item in data_list:
            self.insert_at_end(item)

    def get_length(self):
        next_node = self.head
        count = 0
        while next_node:
            next_node = next_node.next
            count+=1
        return count
    
    def remove_at(self,index):
        if index<0 or index>=self.get_length():
            raise Exception('Invalid Index')
        
        if index == 0:
            self.head = self.head.next
            return
        
        node = self.head
        for i in range(index+1):
            if i == index-1:
                node.next = node.next.next
            node = node.next

    def insert_at(self,index,data):
        if index<0 or index>=self.get_length():
            raise Exception('Invalid Index')
        
        if index == 0:
            self.insert_at_begining(data)
            return
        
        node = self.head
        for i in range(index+1):
            if i == index-1:
                new_node = Node(data,node.next)
                node.next = new_node
            node = node.next
        
    def print(self):
        if self.head == None:
            print('Linked List is Empty')
            return None
        next_node = self.head
        llstr = ''
        while next_node:
            llstr += next_node.data+'-->'
            next_node = next_node.next
        print(llstr)


ll = LinkedList()
ll.insert_at_begining('A')
ll.insert_at_begining('B')
ll.insert_at_begining('C')
ll.insert_at_begining('D')
ll.insert_at_end('E1')
ll.insert_at_end('E2')
ll.insert_at_end('E3')
data_list = ['apple', 'banana', 'mango', 'grapes']
ll.insert_values(data_list)

# ll.remove_at(2)
ll.insert_at(2,'pomo')
ll.insert_at(2,'pomo')
ll.print()
print('Length of Linked List: ', ll.get_length())