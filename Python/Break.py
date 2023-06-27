"""
Break : Break Is a Statement Which Execute At Looping Time

Using Of Break statement We Can Break The Statement

Syntax :

for i in range(1,6):
if condition:
    break
    
    
"""

for i in range(1,6):
    marks = int(input("Enter Marks : "))
    if marks>=35:
        print("Pass")
    else:
        print("You Are Fail...")
        break