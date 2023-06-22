
name = input("Enter your name: ")
gender = input("Enter gender (M/F): ")
age = int(input("Enter age: "))

product = input("Enter product: ")
product_gram = int(input("Enter product gram: "))
current_gold_price = int(input("current gold price (1 grm): "))

total_gold_rate = current_gold_price * product_gram
print(f"TOTAL GOLD RATE: {total_gold_rate}")

making_charges = int(input("Making charges (1 gram): "))
total_making_charges = making_charges * product_gram
print(f"Total Making Charges: {total_making_charges}")

total_amount = total_gold_rate + total_making_charges
print(f"TOTAL AMOUNT: {total_amount}")

if gender == "M":
    if age >= 65:
        if 200000 <= total_amount < 300000:
            discount = 20
        elif 300000 <= total_amount < 500000:
            discount = 30
        elif total_amount >= 500000:
            discount = 35
    else:
        if 200000 <= total_amount < 300000:
            discount = 10
        elif 300000 <= total_amount < 500000:
            discount = 20
        elif total_amount >= 500000:
            discount = 25
elif gender == "F":
    if age >= 65:
        if 200000 <= total_amount < 300000:
            discount = 25
        elif 300000 <= total_amount < 500000:
            discount = 35
        elif total_amount >= 500000:
            discount = 40
    else:
        if 200000 <= total_amount < 300000:
            discount = 15
        elif 300000 <= total_amount < 500000:
            discount = 25
        elif total_amount >= 500000:
            discount = 30
discount_amount = (total_gold_rate + making_charges) /100
print(f"DISCOUNT AMOUNT: {discount_amount}")

total_net_amount = total_amount - discount_amount
print(f"TOTAL NET AMOUNT: {total_net_amount}")
