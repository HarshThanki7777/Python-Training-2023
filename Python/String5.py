status = True

while status:
    num = int(input("Enter Number = "))
    if num%2==0:
        print("Even Number....")
    else:
        print("Odd Number....")
        
        check = input("Do You Want To Continue ? Press Y for Yes And Press N for No :")
        if check == 'y' or check == 'Yes':
            status = True
        else:
            status = False    