#function with parameters and function without return type

# def checkEvenOdd(num):
#     if num%2==0:
#         print("Even Number")
#     else:
#         print("Odd Number")
# num = int(input("Enter Number : "))
# checkEvenOdd(num)        


#Function without Parameter And Function With Return Type

# def checkEvOd():
#     num = int(input("Enter Number : "))
#     if num%2 == 0:
#         return "even Number"
#     else:
#         return "odd Number"
    
# print(checkEvOd())

#Function With Return Type And Function With Parameter

def sum(num1,num2):
    return num1 + num2 

num1 = int(input("Enter Number 1 : "))
num2 = int(input("Enter Number 2 : "))

print(sum(num1,num2))