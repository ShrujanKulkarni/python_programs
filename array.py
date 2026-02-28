class Stack:
    def __init__(self):
        self.stack_list=[]

    def push(self,value):
        self.stack_list.append(value)

    def push_index(self,index,value):
        self.stack_list.insert(index,value)
    
    def pop(self):
        self.stack_list.pop()

    def printlist(self):
        for x in self.stack_list:
            print(x)
    
obj = Stack()
obj.push(10)
obj.push(11)
print("After push")
obj.printlist()

# print("----After Pop----")
# obj.printlist()

print("Insert at index")
obj.push_index(2,50)
print("----After push at index 2 ----")
obj.printlist()
