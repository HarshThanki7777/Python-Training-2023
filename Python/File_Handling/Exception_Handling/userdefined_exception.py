class Checkodddata(Exception):
    pass 

num = int(input("Enter Your Number : "))
try :
    if num%2==0:
        print("Even Number ")
    else:
        raise Checkodddata
except:
    print("odd data entered ")        