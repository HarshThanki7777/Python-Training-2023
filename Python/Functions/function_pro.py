"""
Function : function is a block of code that code are used to again and again.

using of function we can reduce code and save time 

we can call code multiple times 

there are 2 types of function 

1) built-in function
2) user deffined function 

-> built in function :

-> which is predefined by python
    e.g. print(), input(), len(), range().
    

-> user defined function
    a function which is defined by user its called user defined function 
    
    there are 2 steps to create user defined function 
    
    1)function declaration or defination
    2)function calling 
    
    => function defination 
        def <funname>():
        statement
        //block of code...
        

"""

def greetings():
    print("Hello Welcome To python Programming ")

for i in range(1,5):
    greetings()
    