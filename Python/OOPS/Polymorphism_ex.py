"""

Poly Means Many And Morphism Means Forms 

PolyMorPhism Is A Greek Word Which Is Derived Same Name Method With Different Different Forms
there are Mainly 2 Types Of Polymorphism

1) Method Oveloading 
2) Method Overriding

1) Method Overloading : One Class Have More Than 2 Methods With Same Name And
    same Parameters
    
    note : python does not support method overloading
    
2) Method Overriding : Two Class Have Same Name Methods With Same Arguments
            its Called Method Overriding       


"""

class Student:
    def display(self):
        print("This Is Student Class Display")
        
    def display(self,num1,num2):
        self.num1 = num1
        self.num2 = num2
        print(self.num1)
        print(self.num2)
        
obj = Student()
obj.display(12,23)
obj.display()        