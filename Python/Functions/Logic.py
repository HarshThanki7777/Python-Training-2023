def purchase(productname,category,qty,price):
    print("Product Name : ",productname)
    print("category : ",category)
    print("qty : ",qty)
    print("Price : ",price)
    
    totalprice = qty * price
    return totalprice