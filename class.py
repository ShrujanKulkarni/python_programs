class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def printDetails(self):
        print(f"Name is:{self.name}")
        print(f"Age is: {self.age}")

p1= Person("Vani", 32)
p1.printDetails()

p2=Person("SK",34)
p2.printDetails()


