score = 0

def counter():
    global score
    score += 1 
    print(score)
    
    counter()
    counter()