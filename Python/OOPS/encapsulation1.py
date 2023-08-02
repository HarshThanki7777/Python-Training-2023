"""

To Hide Or Prevent Data From Outside The Class 

We Can Use Some Access Specifiers

=> Public 
=> Private 
=> Protected 

By Default All The Members Are Public 

If We Declare Any Variable As Private We Need To Use _ in Prefix

private : Which is Only modify by Current Class 
Protected : Which is modify By Own Class And Child Class 

"""

class Products:
    def __init__(self) -> None:
        self.mobile = 5000
        self._laptop = 26000 #private
        
    def display(self):
            print("laptop : ",self._laptop)
            print("mobile : ",self.mobile)
            
    def changePrice(self,laptopNewPrice):
        self._laptop = laptopNewPrice
        
obj = Products()
obj.display()

obj.mobile = 12000
obj._laptop = 35000

obj.display()

obj.changePrice(45000)

obj.display()
