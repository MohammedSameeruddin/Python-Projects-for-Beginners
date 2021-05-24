import random

choices=["Rock","Paper","Scissors"]
computer_choice=random.choice(choices);
Player_Score=0
Computer_score=0
player_Choice=input("Please enter your choice: ").capitalize()
if(player_Choice==computer_choice):
        print("Tie :)")
elif(player_Choice=="Rock" and computer_choice=="Paper"):
        print("you loose :(")
        Computer_score+=1
elif(player_Choice=="Scissors" and computer_choice=="Rock"):
        print("you loose :) ")
        Computer_score+=1
elif(player_Choice=="paper" and computer_choice=="Scissors"):
        print("you win :) ")
        Player_Score+=1
print("Player final score",Player_Score)
print("Computer Final score",Computer_score)
print("Final Result:____ ")
if(Player_Score>Computer_score):
    print("you win hurrah")
elif(Player_Score<Computer_score):
    print("Computer wins")
elif(Player_Score==Computer_score):
    print("Game Tie")


      
