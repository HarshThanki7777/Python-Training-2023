subject_marks = int(input("Enter Subject Marks :"))

if subject_marks >=0 and subject_marks <=100:
    if subject_marks >=70:
        print("You Passed With Distinction")
    elif subject_marks >=60:
        print("You Are Passed With B Grade") 
    elif subject_marks >=50:
        print("You Are Passed With C Grade")
    elif subject_marks >=40:
        print("You Are Passed With D Grade") 
    elif subject_marks >=30:
        print("You Are Passed")
    
    else  :
        print("You Are Fail In Exam")       
else :
    print("Invalid Input") 