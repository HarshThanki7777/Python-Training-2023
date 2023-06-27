# """
# Continue Is a Statement Which Skip Current Statement

# """

# for i in range(1,10):
#     if i==3 or i==5:
#         continue
#     else:
#         print(i)
    

for i in  range(1,100):
    num = float(input("Enter Your Number :"))
    if num >= 0:
        continue
    else:
        print("Negative Number")
        break