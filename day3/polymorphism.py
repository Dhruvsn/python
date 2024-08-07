class A:
    def __init__(self):
        self.x= 10
        self.y = 20

    def fun1(self):
        print("This is fun1 from class A")
    
    def printmember(self):
        print(self.y)
        print(self.x)

class B(A):
    def __init__(self):
        super().__init__()  # Call the parent class's __init__ method
        self.a = 11
        self.b = 22

    def fun1(self):
        print("This is fun1 from class B")
    
   


if __name__ == "__main__":
    obj = B()
    print(obj.a)
    print(obj.b)
    obj.printmember()
    obj.fun1()  

    

  


