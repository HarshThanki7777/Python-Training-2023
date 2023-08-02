try:
    num1 = int(input("Enter Number 1 : "))
    num2 = int(input("Enter Number 2 : "))
    
    ans = num1 / num2 
    print(ans)
    
except ValueError:
    print("int Value Required")
except ZeroDivisionError:
    print("Cannot Be Divided By Zero")        