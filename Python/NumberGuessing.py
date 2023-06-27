import random 

computer = random.randint(1,100)

status = True
while status:
    num = int(input("Enter Number :"))
    if num > computer:
        print("HINT : Guess Lower Number ")
    elif num > computer:
        print("HINT : Guess Upper Number ") 
    else:
        print("You Win!!!") 
        status = False      