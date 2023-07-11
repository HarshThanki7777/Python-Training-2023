#Calculator using Function

menu = """
        
                    MENU 
                    
                    press 1 for addition 
                    press 2 for multiplication
                    press 3 for substraction
                    press 4 for division

        """
        
def sum():
        num1 = int(input("Enter Number 1 : "))
        num2 = int(input("Enter Number 2 : "))
        
def mul():
    num1 =int(input("Enter Number 1 : "))
    num2 =int(int("Enter Number 2 : "))        
    ans = num1 * num2 
    print(ans)
    
    status = True 
    while status:
        print(menu)
        choice = int(input("Enter Your Choice : "))
        if choice == 1:
            sum()
        elif choice == 2:
            mul()
            
            continue_choice = input("Do You Want To Perform More Operations Press Y for Yes and Press N for No :")    
            if continue_choice == 'y':
                status = True
            else:
                status = False    