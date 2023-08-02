"""

Multiple Inheritance 

            A                   B
            |                   |
            --------------------
                        |
                        V
                        C

"""

class A :
        def __init__(self,n1,n2) -> None:
            self.num1 = n1 
            self.num2 = n2
        
class B(A): 
    def __init__(self,n1,n2) -> None:
        super().__init__(n1, n2)
    def display(self):
        print(self.num1)
        print(self.num2)
        print(self.num1 + self.num2)
        
class C(A):
    def display(self) :
        self.inputA()
        self.ans = A.num1 * A.num2
        print("ans = ",self.ans)
b = B(10,20)
b.display()        