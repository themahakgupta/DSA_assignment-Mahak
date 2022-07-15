class Stack:
    def __init__(self):
        self.data = []
          
    def push(self, value):
        self.data.append(value)
    
    def pop(self):
        return self.data.pop()
    def empty(self):
        return self.data == []
      
    def show(self):
        for value in reversed(self.data):
            print(value)
  
def atbottom(s, value):
    if s.empty(): 
        s.push(value)
    else:
        popped = s.pop()
        atbottom(s, value)
        s.push(popped)
  
def Reverse(s):
    if s.empty():
        pass
    else:
        popped = s.pop()
        Reverse(s)
        atbottom(s, popped)
stack_output = Stack()
  
stack_output.push(1)
stack_output.push(2)
stack_output.push(3)
stack_output.push(4)
stack_output.push(5)
  
print("Original Stack")
stack_output.show()
  
print("\nStack after Reversing")
Reverse(stack_output)
stack_output.show()
