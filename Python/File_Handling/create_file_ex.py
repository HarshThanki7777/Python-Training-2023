f = open("file_ex2.txt","a")

for i in range(1,3):
    name = input("Enter Your Name : ")
    score = int(input("Enter Your Score : "))
    f.write("\n"+name)
    f.write("\n"+str(score))
    
    f.close()
    
    f = open("file_ex2.txt","r")
    print(f.read())
    
    f.close()