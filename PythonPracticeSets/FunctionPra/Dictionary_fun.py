#Food billing System

menu = {
    "Burger": 45,
    "Pizza": 110,
    "Fries": 80,
    "coldrinks": 20,
    "Chips": 10
}

def display_menu():
    print("Menu : ")
for item, price in menu.items():
    print(f"{item}: Rs {price}")
        
def calculate_total(order):#order justify invokes
    total = 0 
    for item in order:
        if item in menu:
            total += menu[item]
        else:
            print(f"Not Available This Item: {item}")
    return total   #  #Functions are often designed to perform a specific task or computation and provide the result back to the caller. The return statement allows you to send the computed result back to the calling code.       
    
def apply_discount(total, discount):
    discount_amount = total * (discount/100)
    return total - discount_amount

def calculate_tax(total, tax_rate):
    tax_amount = total * (tax_rate/100)
    return total + tax_amount

def generate_receipt(order, total, discount, tax_rate):
    print("----------Receipt----------")
    for item in order:
        print(f"{item}: {menu[item]}")
        print("----------------------------")
        print(f"Subtotal: Rs{total:.2f}")
        print(f"Discount: {discount}%")
        total_with_discount = apply_discount(total, discount)
        print(f"Total After discount: Rs{total_with_discount:.2f}")
        total_with_tax = calculate_tax(total_with_discount,tax_rate)
        print(f"Total With Tax : Rs{total_with_tax:.2f}")
        print("------------------------------------")
        print("Thank you For Your Order!")
        
def main():
    display_menu()
    order = input("Enter your order (comma-separated items): ").split(",")
    total = calculate_total(order)

    discount = float(input("Enter discount percentage (0 if none): "))
    total_with_discount = apply_discount(total, discount)

    tax_rate = float(input("Enter tax rate percentage (0 if none): "))
    total_with_tax = calculate_tax(total_with_discount, tax_rate)

    generate_receipt(order, total, discount, tax_rate)

if __name__ == "__main__":
    main()