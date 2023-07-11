quiz = {
    1: {
        
        "que" : "most popular programming language ?",
        "ans" : "python"
    },
    2: {
        "que" : "Most Popular Cricketer",
        "ans" : "ms dhoni"
    },
    3: {
        "que":"Prime Minister Of India ?",
        "ans" : "narendra modi"
    }
}

score = 0

for i in range(1,len(quiz)+1):
    print(f"Que.{i} {quiz[i]['que']}")
    
    ans = input("Enter Your Ans : ").lower()
    if quiz[i]['ans'] == ans:
        print("Right Answer")
        score+=50
        print(f"score = {score}")    
    else:
        score-=20
        print("Wrong Answer").lower()
        
        print(f"score = {score}")    
        
        