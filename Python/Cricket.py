import random

Team = """
        1.CHENNAI SUPER KINGS,
        2.DELHI CAPITALS
        3.GUJARAT TITANS
        4.KOLKATA KNIGHT RIDERS
        5.LUCKNOW SUPER GIANTS
        6.MUMBAI INDIANS
        7.PUNJAB KINGS
        8.RAJASTHAN ROYALS
        9.ROYAL CHALLANGE BANGALORE
        10.SUNRISE HYDERABAD
        """
print("List of Team : \n",Team)
print("========================================================================================================\n")

team_list = ["CHENNAI SUPER KINGS","DELHI CAPITALS","GUJARAT TITANS","KOLKATA KNIGHT RIDERS","LUCKNOW SUPER GIANTS","MUMBAI INDIANS","PUNJAB KINGS","RAJASTHAN ROYALS","ROYAL CHALLANGE BANGALORE","SUNRISE HYDERABAD"]
toss_list = ["HEAD","TAILS"]
play_list = ["BATTING","BOWLING"]
run_list = ["1","2","3","4","6","NO BOWL","WIDE BOWL","WICKET"]
status = True
my_score = 0
my_wicket = 0
computer_score = 0
computer_wicket = 0
my_play = 0

while status:

    my_team = int(input("Please Select Your Team by Entering Number 1 to 10 :"))
    print("\n========================================================================================================\n")
    print("Your Team  : ",team_list[my_team-1])

    computer_team=random.choice(team_list)
    print("Computer Team : ",computer_team)
    team_list.remove(computer_team)

    if my_team == computer_team :
        print("Both Player Select Same Team Please Select Diffrent Team to Play")

    print("\n============================   Its Time For Toss   ======================================================\n")

    my_toss = input("Please Select HEAD/TAILS :").upper()
    if my_toss == "TAILS" or my_toss == "HEAD" :

        computer_toss = random.choice(toss_list)
    
        if my_toss == computer_toss :
            print("You Won Toss !!!")
            
            print("\n======================  TIme to Select BATTING/BOWLING  =============================================\n")
                    
            my_play = input("Press 1 for BATTING or 2 for BOWLING : ")

            if my_play == "1" or my_play == "BATTING":

                print("\n======================  Press Enter for BATTING  =============================================\n")
                i=1
                while i<=6 :
                    auto_run = random.choice(run_list)
                    input("PRESS ENTER TO NEXT : ")

                    if auto_run =="1":
                        my_score+=1
                        my_wicket+=0
                        print("Score : ", my_score ,"/",my_wicket,"Ball : ",(i/10))
                        i+=1

                    elif auto_run =="2":
                        my_score+=2
                        my_wicket+=0
                        print("Score : ", my_score ,"/",my_wicket,"Ball : ",(i/10))
                        i+=1

                    elif auto_run =="3":
                        my_score+=3
                        my_wicket+=0
                        print("Score : ", my_score ,"/",my_wicket,"Ball : ",(i/10))
                        i+=1

                    elif auto_run =="4":
                        my_score+=4
                        my_wicket+=0
                        print("Score : ", my_score ,"/",my_wicket,"Ball : ",(i/10))
                        i+=1

                    elif auto_run =="6":
                        my_score+=6
                        my_wicket+=0
                        print("Score : ", my_score ,"/",my_wicket,"Ball : ",(i/10))
                        i+=1

                    elif auto_run =="NO BOWL":
                        my_score+=1
                        my_wicket+=0
                        print("NO BALL !!!!!!")
                        print("Score : ", my_score ,"/",my_wicket,"Ball : ",(i/10))
                        
                    elif auto_run =="WIDE BOWL":
                        my_score+=1
                        my_wicket+=0
                        print("WIDE BALL !!!!!!!!!!!")
                        print("Score : ", my_score ,"/",my_wicket,"Ball : ",(i/10))
                        i+=1
                        
                    elif auto_run =="WICKET":
                        my_score+=1
                        my_wicket+=1
                        print("WICKET !!!!!!!!!")
                        print("Score : ", my_score ,"/",my_wicket,"Ball : ",(i/10))
                        i+=1
                input("PRESS ENTER TO SHOW FINAL SCORE")

                print("\n======================  Final Score  =============================================\n")
                
                print(my_score,"/",my_wicket)
            else :
                print("\n======================  Press Enter for BOWLING  =============================================\n")
                i=1
                while i<=6 :
                    auto_run = random.choice(run_list)
                    input("PRESS ENTER NEXT : ")

                    if auto_run =="1":
                        computer_score+=1
                        computer_wicket+=0
                        print("Score : ", computer_score ,"/",computer_wicket,"Ball : ",(i/10))
                        i+=1

                    elif auto_run =="2":
                        computer_score+=2
                        computer_wicket+=0
                        print("Score : ", computer_score ,"/",computer_wicket,"Ball : ",(i/10))
                        i+=1

                    elif auto_run =="3":
                        computer_score+=3
                        computer_wicket+=0
                        print("Score : ", computer_score ,"/",computer_wicket,"Ball : ",(i/10))
                        i+=1

                    elif auto_run =="4":
                        computer_score+=4
                        computer_wicket+=0
                        print("Score : ", computer_score ,"/",computer_wicket,"Ball : ",(i/10))
                        i+=1

                    elif auto_run =="6":
                        computer_score+=6
                        computer_wicket+=0
                        print("Score : ", computer_score ,"/",computer_wicket,"Ball : ",(i/10))
                        i+=1

                    elif auto_run =="NO BOWL":
                        computer_score+=1
                        computer_wicket+=0
                        print("NO BALL !!!!!!")
                        print("Score : ", computer_score ,"/",computer_wicket,"Ball : ",(i/10))
                        
                    elif auto_run =="WIDE BOWL":
                        computer_score+=1
                        computer_wicket+=0
                        print("WIDE BALL !!!!!!!!!!!")
                        print("Score : ", computer_score ,"/",computer_wicket,"Ball : ",(i/10))
                        i+=1

                    elif auto_run =="WICKET":
                        computer_score+=1
                        computer_wicket+=1
                        print("WICKET !!!!!!!!!")
                        print("Score : ", computer_score ,"/",computer_wicket,"Ball : ",(i/10))
                        i+=1
                input("PRESS ENTER TO SHOW FINAL SCORE")

                print("\n======================  Final Score  =============================================\n")
                
                print(computer_score,"/",computer_wicket)
            
        else:
            print("Computer Won Toss !!!")
            input("\n======================  TIme to Select BATTING/BOWLING  =============================================\n")
            computer_play = random.choice(play_list)
            print("Computer Select : ",computer_play)

            if computer_play == "BATTING":
                my_play = "BOWLING"
                print("\n======================  Press Enter for BOWLING  =============================================\n")
                i=1
                while i<=6 :

                    auto_run = random.choice(run_list)
                    input("PRESS ENTER NEXT : ")

                    if auto_run =="1":
                        computer_score+=1
                        computer_wicket+=0
                        print("Score : ", computer_score ,"/",computer_wicket,"Ball : ",(i/10))
                        i+=1

                    elif auto_run =="2":
                        computer_score+=2
                        computer_wicket+=0
                        print("Score : ", computer_score ,"/",computer_wicket,"Ball : ",(i/10))
                        i+=1

                    elif auto_run =="3":
                        computer_score+=3
                        computer_wicket+=0
                        print("Score : ", computer_score ,"/",computer_wicket,"Ball : ",(i/10))
                        i+=1

                    elif auto_run =="4":
                        computer_score+=4
                        computer_wicket+=0
                        print("Score : ", computer_score ,"/",computer_wicket,"Ball : ",(i/10))
                        i+=1

                    elif auto_run =="6":
                        computer_score+=6
                        computer_wicket+=0
                        print("Score : ", computer_score ,"/",computer_wicket,"Ball : ",(i/10))
                        i+=1

                    elif auto_run =="NO BOWL":
                        computer_score+=1
                        computer_wicket+=0
                        print("NO BALL !!!!!!")
                        print("Score : ", computer_score ,"/",computer_wicket,"Ball : ",(i/10))
                        
                    elif auto_run =="WIDE BOWL":
                        computer_score+=1
                        computer_wicket+=0
                        print("WIDE BALL !!!!!!!!!!!")
                        print("Score : ", computer_score ,"/",computer_wicket,"Ball : ",(i/10))
                        i+=1

                    elif auto_run =="WICKET":
                        computer_score+=1
                        computer_wicket+=1
                        print("WICKET !!!!!!!!!")
                        print("Score : ", computer_score ,"/",computer_wicket,"Ball : ",(i/10))
                        i+=1
                input("PRESS ENTER TO SHOW FINAL SCORE")

                print("\n======================  Final Score  =============================================\n")
                
                print(computer_score,"/",computer_wicket)
            else:
                print("\n======================  Press Enter for BATTING  =============================================\n")
                my_play = "BATTING"

                i=1
                while i<=6 :
                    
                    auto_run = random.choice(run_list)
                    input("PRESS ENTER NEXT : ")

                    if auto_run =="1":
                        my_score+=1
                        my_wicket+=0
                        print("Score : ", my_score ,"/",my_wicket,"Ball : ",(i/10))
                        i+=1

                    elif auto_run =="2":
                        my_score+=2
                        my_wicket+=0
                        print("Score : ", my_score ,"/",my_wicket,"Ball : ",(i/10))
                        i+=1

                    elif auto_run =="3":
                        my_score+=3
                        my_wicket+=0
                        print("Score : ", my_score ,"/",my_wicket,"Ball : ",(i/10))
                        i+=1

                    elif auto_run =="4":
                        my_score+=4
                        my_wicket+=0
                        print("Score : ", my_score ,"/",my_wicket,"Ball : ",(i/10))
                        i+=1

                    elif auto_run =="6":
                        my_score+=6
                        my_wicket+=0
                        print("Score : ", my_score ,"/",my_wicket,"Ball : ",(i/10))
                        i+=1

                    elif auto_run =="NO BOWL":
                        my_score+=1
                        my_wicket+=0
                        print("NO BALL !!!!!!")
                        print("Score : ", my_score ,"/",my_wicket,"Ball : ",(i/10))
                        
                    elif auto_run =="WIDE BOWL":
                        my_score+=1
                        my_wicket+=0
                        print("WIDE BALL !!!!!!!!!!!")
                        print("Score : ", my_score ,"/",my_wicket,"Ball : ",(i/10))
                        i+=1

                    elif auto_run =="WICKET":
                        my_score+=1
                        my_wicket+=1
                        print("WICKET !!!!!!!!!")
                        print("Score : ", my_score ,"/",my_wicket,"Ball : ",(i/10))
                input("PRESS ENTER TO SHOW FINAL SCORE")

                print("\n======================  Final Score  =============================================\n")
                
                print(my_score,"/",my_wicket)

        print("\n ########################################  NOW FOR SECOND TEAM  ###############################################\n")
        
        if my_play == "1" or my_play == "BATTING":

            print("\n======================  Press Enter for BOWLING  =============================================\n")
            i=1
            while i<=6 :
                    auto_run = random.choice(run_list)
                    input("PRESS ENTER NEXT : ")

                    if auto_run =="1":
                        computer_score+=1
                        computer_wicket+=0
                        print("Score : ", computer_score ,"/",computer_wicket,"Ball : ",(i/10))
                        i+=1

                    elif auto_run =="2":
                        computer_score+=2
                        computer_wicket+=0
                        print("Score : ", computer_score ,"/",computer_wicket,"Ball : ",(i/10))
                        i+=1

                    elif auto_run =="3":
                        computer_score+=3
                        computer_wicket+=0
                        print("Score : ", computer_score ,"/",computer_wicket,"Ball : ",(i/10))
                        i+=1

                    elif auto_run =="4":
                        computer_score+=4
                        computer_wicket+=0
                        print("Score : ", computer_score ,"/",computer_wicket,"Ball : ",(i/10))
                        i+=1

                    elif auto_run =="6":
                        computer_score+=6
                        computer_wicket+=0
                        print("Score : ", computer_score ,"/",computer_wicket,"Ball : ",(i/10))
                        i+=1

                    elif auto_run =="NO BOWL":
                        computer_score+=1
                        computer_wicket+=0
                        print("NO BALL !!!!!!")
                        print("Score : ", computer_score ,"/",computer_wicket,"Ball : ",(i/10))
                
                    elif auto_run =="WIDE BOWL":
                        computer_score+=1
                        computer_wicket+=0
                        print("WIDE BALL !!!!!!!!!!!")
                        print("Score : ", computer_score ,"/",computer_wicket,"Ball : ",(i/10))
                        i+=1

                    elif auto_run =="WICKET":
                        computer_score+=1
                        computer_wicket+=1
                        print("WICKET !!!!!!!!!")
                        print("Score : ", computer_score ,"/",computer_wicket,"Ball : ",(i/10))
                        i+=1
                
            input("PRESS ENTER TO SHOW FINAL SCORE")

            print("\n======================  Final Score  =============================================\n")
                
            print(computer_score,"/",computer_wicket)

        else :
                print("\n======================  Press Enter for BATTING  =============================================\n")

                i=1
                while i <= 6 :
                    
                    auto_run = random.choice(run_list)
                    input("PRESS ENTER TO NEXT :")

                    if auto_run =="1":
                        my_score+=1
                        my_wicket+=0
                        print("Score : ", my_score ,"/",my_wicket,"Ball : ",(i/10))
                        i+=1

                    elif auto_run =="2":
                        my_score+=2
                        my_wicket+=0
                        print("Score : ", my_score ,"/",my_wicket,"Ball : ",(i/10))
                        i+=1

                    elif auto_run =="3":
                        my_score+=3
                        my_wicket+=0
                        print("Score : ", my_score ,"/",my_wicket,"Ball : ",(i/10))
                        i+=1

                    elif auto_run =="4":
                        my_score+=4
                        my_wicket+=0
                        print("Score : ", my_score ,"/",my_wicket,"Ball : ",(i/10))
                        i+=1

                    elif auto_run =="6":
                        my_score+=6
                        my_wicket+=0
                        print("Score : ", my_score ,"/",my_wicket,"Ball : ",(i/10))
                        i+=1

                    elif auto_run =="NO BOWL":
                        my_score+=1
                        my_wicket+=0
                        print("NO BALL !!!!!!")
                        print("Score : ", my_score ,"/",my_wicket,"Ball : ",(i/10))

                    elif auto_run =="WIDE BOWL":
                        my_score+=1
                        my_wicket+=0
                        print("WIDE BALL !!!!!!!!!!!")
                        print("Score : ", my_score ,"/",my_wicket,"Ball : ",(i/10))
                        i+=1

                    elif auto_run =="WICKET":
                        my_score+=1
                        my_wicket+=1
                        print("WICKET !!!!!!!!!")
                        print("Score : ", my_score ,"/",my_wicket,"Ball : ",(i/10))
                        i+=1

                input("PRESS ENTER TO SHOW FINAL SCORE")

                print("\n======================  Final Score  =============================================\n")
                
                print(my_score,"/",my_wicket)
                            
        print("\n **********************************  Result Time  ********************************************\n")
        input("Press Enter To Show Result : ")


        print("My Team Score :",my_score,"/",my_wicket)
        print("Computer Team Score :",computer_score,"/",computer_wicket)

        print("\n ******************************************************************************\n")
        if my_score > computer_score:
            print("You Won Match !!!")
        else:
            print("Computer Won Match !!!")
    else: 
        print("Please Enter valid Input: HEAD/TAILS")    
        
    check = input("\n Do you want to Play Again ??? \n press y for Yes or n for No :").upper()
    if check == "N":
        status = False