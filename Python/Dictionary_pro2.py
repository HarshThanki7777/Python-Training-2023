role = """
        
        MENU 
        
        press 1 for Shopper
        press 2 for Cutomer


"""

#created dictionary 
products = {} #created blank dictionary Here

#created Shoppingcart Dictionary
shopping_cart = {}
status = True
while status :
    print(role)
    choice = int(input("Enter Your Choice : "))
    
    if choice == 1:
        specific = {} #created Blank dictionary for specific product values
        
        product_name = input("Enter Product Name : ")
        qty = int(input("Enter Product qty : "))
        price = int(input("Enter Product Price : "))
        
        
        if product_name in products :
            old_qty = products[product_name]['qty']
            specific['qty'] = qty + old_qty
            specific['price'] = price
            
            #print(specific)
        else: 
            specific["qty"] = qty
            specific['price'] = price
            #print(specific)
            
            products[product_name] = specific
            
            #print(products)
            next_choice = input("Do You Want To Continue ? Press Y For Yes And Press N For No : ")
            if next_choice == 'y':
                status = True
            else:
                status = False
                
                
    else:
        print("                    Welcome To Cutomer Panel           ") 
        print("        Menu         ")
        for  k,v in products.items():
            print(f"{k} Qty={v['qty']} Rs. {v['price']}") 
            
            name = input("Enter Product Name : ")
            if name in products.keys():
                print("Yes, Product Is Available")
                
                qty = int(input("Enter qty : "))
                
                total_price = products[name]['price']*qty
                
                print("total price = ",total_price)             