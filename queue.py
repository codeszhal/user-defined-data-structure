class Queue:
    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        return self.items == []
    
    def enqueue(self, fitur):
        self.items.insert(0, fitur)
    
    def dequeue(self):
        self.items.pop()
    
    def print_queue(self):
        print(self.items)

q = Queue()
q.enqueue('a')
q.enqueue('b')
q.enqueue('42')
q.print_queue()

q.dequeue()
q.print_queue()