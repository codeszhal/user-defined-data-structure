'''
Stack

You need to make a back button for a browser.
You use a stack to store the website links visited. Each new link visited is pushed onto the stack.
The back button needs to pop the top link from the stack and navigate to it.

The given code declares a Browser class as a stack and implements some of its methods. Then, some links are pushed onto the stack.
A while loop is then used to go back to all links and print them.

Implement the required pop() method for the Browser, so that the given code works as expected.
'''

class Browser:
    def __init__(self):
      self.items = []  
  
    def is_empty(self):
      return self.items == []
  
    def push(self, items):
      self.items.insert(0, items)
    
    def pop(self):
      p = self.items[0]
      self.items.pop(0)
      return p
    
    
  
x = Browser()
x.push('about:blank')
x.push('www.koonek.net')
x.push('www.koonek.net/layanan/')
x.push('www.koonek.net/layanan/konsultan-jaringan')

while not x.is_empty():
    print(x.pop())