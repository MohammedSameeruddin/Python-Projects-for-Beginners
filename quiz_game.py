

def quiz(guess,answer):
    global score;
    still_guessing=True
    attempts=0
    while still_guessing and attempts<3:
        if(guess.upper()==answer.upper()):
            print("your answer is correct")
            score=score+1
            still_guessing=False
        elif(attempts<2):
            print(input("Wrong answer, try again please"))
            attempts=attempts+1
    if(attempts==3):
        print("your correct answer is",answer)
        
score=0
print("guess the capital")
capital=str(input("what is capital of INDIA"))
quiz(capital,"DELHI")

print("guess the animal")
ANIMAL=str(input("what is national animal of INDIA"))
quiz(ANIMAL,"TIGER")

print("guess the bird")
BIRD=str(input("what is national BIRD of INDIA"))
quiz(BIRD,"PEACOCK")

print("Your Score is "+ str(score))
            
