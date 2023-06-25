num = int(input("Enter The Range Of The Fibonacci Series :"))

a,b = 0,1
count = 0


if num < 0 :
    print("Please Enter Positive Number :")
elif num == 1 :
    print (f"Fibonacci Sequence Upto {num} :")
    print(a)
else :
    print(f"Fibonacci Sequence Upto {num} :") 
    while count < num:
        print(a, end='')
        c = a + b
        a = b 
        b = c
        count += 1