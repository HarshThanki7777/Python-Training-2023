"""
Inheritance : inheritance 
                
                one class Derived Properties Of Another class 
                Its Called Inheritance 
                
                
                Inheritance Provides Reusabilities there are Mainly 5 
                Types Of Inheritance 
                
                1) Single Level Inheritance
                2) Multi Level Inhertiance
                3) Hierarchical Inheritance
                4) Multi-ple Inheritance 
                5) Hybrid Inheritance

1) Single Level Inheritance :
            
            one class derived Properties Of Another Class 
            
                            A
                            |
                            v
                            
                            B
"""

class Parent :
    def Bike(self):
        print("I Have Bike")
        
class child(Parent):
    def cycle(self):
        print("I Have My Own Cycle")
        
# Object Creation
obj = child()
obj.Bike()
obj.cycle()        