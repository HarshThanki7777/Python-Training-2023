# The continue statement in Python is used to skip the rest of the code inside a loop for the current iteration and 
# move on to the next iteration of the loop. It is often used in situations where you want to 
# skip over certain elements or conditions while iterating over a sequence.

for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(i)
