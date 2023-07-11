# jay bhavani food billing system 

# we create 2 roles here , manager and customer 

role = """  
                        MENU 

                    press 1 for manager 
                    press 2 for customer 

        """

# create dictionary 
products = {}   # creating blank dictionary here.

# create shoppingcart dictionary 
shopping_cart = {} 
status = True 
while status:
    print(role)
    choice = int(input("Enter your choice : "))
    
    if choice == 1: 
        specific = {} # creating blank dictionary for specific product values 

        product_name = input("Enter product name : ")
        qty = int(input("Enter product qty : "))
        price = int(input("Enter product price : "))

    
        if product_name in products:
            old_qty = products[product_name]['qty']
            specific['qty'] = qty + old_qty
            specific['price'] = price

            #print(specific)    
        else:
            specific['qty'] = qty 
            specific['price'] = price
            #print(specific)    

        products[product_name] = specific

        #print(products)
        next_choice = input("Do you want to continue ? press y for yes and press n for no : ")
        if next_choice == 'y' :
            status = True
        else:
            status = False
        
    else:
        print("                 WELCOME TO CUSTOMER PANEL            ")
        print("     MENU      ")
        for k,v in products.items():
            print(f"{k}   Qty= {v['qty']}  Rs. {v['price']} ")

        name = input("Enter product name : ")
        if name in products.keys():
            print("Yes, product is available")

            qty = int(input("Enter qty : "))

            total_price = products[name]['price'] * qty 

            print("total price = ",total_price)

        

    




















