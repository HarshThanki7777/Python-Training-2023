try :
    num1 = int(input("Enter Your Number 1 : "))
    num2 = int(input("Enter Your Number 2 :"))
    
    ans = num1/num2
except Exception as e :
    print(e)
else:
    print(ans)
finally:
    print("Thank You For Using Application")                
    