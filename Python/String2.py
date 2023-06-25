Email = "HarshThanki203@gmail.com"
Password = "11223344"

u_email = input("Enter Email :")
u_password = input("Enter Password :")

if u_email != Email or  u_password != Password:
    if  u_email!=Email and u_password!=Password:
        print("Invalid Email And Password....")
    elif u_email != Email:
        print("Your Email Is Invalid.....")
    elif u_password != Password:
        print("Your Password Is Invalid.....")
else:    
        print("Valid Email And Password....")