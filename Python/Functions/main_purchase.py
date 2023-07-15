import Logic

product_name = input("Enter Product Name : ")
product_qty = int(input("Enter Product Qty : "))
produt_category = input("Enter Product Category : ")
product_price = int(input("Enter Product Price : "))

print(Logic.purchase(product_name,produt_category,product_qty,product_price))