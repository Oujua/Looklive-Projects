import random
print("rock!")
print("paper!")
print("scissors!")
Pscore = 0
Cscore = 0
win_condition = 5
while Pscore < win_condition and Cscore < win_condition:
    p1 = input("Player 1, Please enter your choice!\n").lower()
    Computer = random.randint(1,3)
    if Computer == 1:
        Computer = "rock"
    elif Computer == 2:
        Computer = "paper"
    elif Computer == 3:
        Computer = "scissors"
    print("Computer plays: " + Computer)
    if p1 == "rock":
        if Computer == "scissors":
            print("Player 1 wins!")
            Pscore += 1
        elif Computer == "paper":
            print("Computer wins!")
            Cscore += 1
        elif p1 == "paper":
            if Computer == "rock":
                print("Player 1 wins!")
                Pscore += 1
            elif Computer == "scissors":
                print("Computer wins!")
                Cscore += 1
        elif p1 == "scissors":
            if Computer == "paper":
                print("Player 1 wins!")
                Pscore += 1
            elif Computer == "rock":
                print("Computer wins!")
                Cscore += 1
        elif p1 == Computer:
            print("Tie!")
        else:
            print("Error.")
    print(f"The score is currently:\n")
    print(f"Player: {Pscore}\n")
    print(f"Computer: {Cscore}\n")
if Pscore > Cscore:
    print (f"Player wins the first to {win_condition}!")
elif Cscore > Pscore:
    print (f"Computer wins the first to {win_condition}!")
else:
    print (f"The first to {win_condition} resulted in a tie.")
