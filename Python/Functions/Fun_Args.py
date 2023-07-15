"""
args : arguments - function With Arguments 
tuple As a Parameter

"""

def myfun(*args):
    sum = 0
    for i in args:
        sum += i
        
    return sum

print(myfun(1,2,3,4,5,6,7))    
    