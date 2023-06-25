num = int(input("Enter Your Number"))

factorial = 1

if num < 0 :
    print("Sorry Factorial Does Not Exist In Negative Numbers !")
elif num == 0 :
    print("Your Factorial of 0 Is 1")
else :
    for i in range(1,num+1) :
        factorial = factorial * i
        print(f"Your Factorial Of {num} is {factorial}")
        
'''
In Python, the `f` in `print(f"Hello, My name is {name} and I'm {age} years old.")` is used to create an f-string,
which is a way to format strings that was introduced in Python 3.6¹. F-strings provide a concise and convenient way to embed expressions inside string literals for formatting².
The expressions inside the curly braces `{}` are evaluated at runtime and their values are inserted into the string³.

F-strings are faster, more readable, more concise, and less prone to error than other ways of formatting strings¹. They can be used to format strings in a more elegant and straightforward way than using the `format()` 
method or other string formatting mechanisms¹. Is there anything else you would like to know? 😊


'''     