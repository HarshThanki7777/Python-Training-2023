"""
Encapsulation : Which Is Behave Like Capsule

which Is Contain Data Member And Member Function In Single Entity

encapsulation which is represent data member in group 

best example of encapsulation is a class 


"""

class Shop:
    def setProduct(self,productName):
        self.productname = productName
        
    def getProduct(self):
        return self.productname
    
    
obj = Shop()
obj.setProduct("Mobile")
print(obj.getProduct())        