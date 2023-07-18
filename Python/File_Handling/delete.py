filename = "data.txt"

file = open(filename,"w")

file.truncate(0)

file.close()

print("Data Deleted Successfully")