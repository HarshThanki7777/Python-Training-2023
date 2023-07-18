import os

if os.path.exists("myfolder"):
    print("Already Folder Created")
else:
    os.mkdir("myfolder")    