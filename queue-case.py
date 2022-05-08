'''
Queue


You are making a call center application, which should handle customers in a queue.
The CallCenter class is implemented as a Queue. Each element of the queue has the topic of the call as its value. The two possible values are 'general' and 'technical'. A 'general' call takes on average 5 minutes to handle, while a 'technical' call requires 10 minutes.
The given code adds multiple customers to the Queue from user input.
You need to dequeue all added customers, calculate and output the total time required to handle all calls.
'''

class CallCenter:
    def __init__(self):
      self.customers = []

    def is_empty(self):
      return self.customers == []

    def add(self, x):
      self.customers.insert(0, x)

    def pop(self):
      return self.customers.pop()


c = CallCenter()

while True:
    n = input()
    if n == 'end':
        break
    c.add(n)

#print(c.customers.pop() == "general")

i = 0
counter = 0
while i < len(c.customers):
    if c.customers.pop() == "general":
        counter += 5 
    else:
        counter += 10
print(counter)
