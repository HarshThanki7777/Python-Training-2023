# In Python, float is a built-in data type that represents real numbers,
# defined as a number with a decimal point dividing the integer and fractional parts.
# The float() function is used to convert a number or a string representation of a numeric value into a floating-point number. For example,
# you can use the float() function to convert an integer into a floating-point number, like this: x = float(3) which returns 3.0.

num = float(input("Enter Your Number :"))

if num > 0:
    print("Positive Number...")
elif num == 0:
    print("Zero")
else :
    print("Negative Number....")    