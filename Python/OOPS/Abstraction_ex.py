"""
Abstraction : Which Is Represent Only few Information
not Allocated Background Information

Abstraction Which Is Provide Only Front Information 

abstraction concept hide implements from outside The World

In Python Using ABC (Abstract Base Class ) We Can Use This Concept 

"""

from abc import ABC 

class RBI(ABC):
    def roi(self):
        pass
    
class SBI(RBI):
    def roi(self):
        print("8.5")
        
class HDFC(RBI):
    def display(self):
        print("Welcome hdfc")
        
    def roi(self):
        print("7.5")    

sbi = SBI()
sbi.roi()
hdfc = HDFC()        
hdfc.roi()
hdfc.display()