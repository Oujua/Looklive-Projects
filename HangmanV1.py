import random
Word_List = list(range(1,126))
Guess_List = []
inFile = open('Hangman_Answers.txt', 'r')
counter = 0
Wrong_Guess = 0
User_Input = "Placeholder"
Word_List.append("Placeholder")
Guess_List.append("Letters used:")
for line in inFile:
    Word_List[counter] = line
    counter += 1
Original_Word = Word_List[random.randint(1,126)]
Original_Word = Original_Word.replace("\n","")
#print(Original_Word) For Dev Purposes
print("You have 2 different options: enter quit to exit the game, or, enter a letter to guess.\n")
Man = """|_________|
|
|
|
|
|"""
Current_Guess = "-" * len(Original_Word)                               # Create variable Current_Guess to contain the current guess
while Original_Word != Current_Guess and User_Input != "quit":          # if still not complete, or user does not choose to quit
    print(Current_Guess)
    User_Input = input("\nEnter a character: ")
    if User_Input in Original_Word:
        print(f"\nYes! {User_Input}, is in the word!")
        new = ""
        for i in range(len(Original_Word)):
            if User_Input == Original_Word[i]:
                new += User_Input                # fill the position with new value
            else:
                new += Current_Guess[i]           # same value as before
        Current_Guess = new
        if Original_Word == Current_Guess:
            print(f"The word was: {Original_Word}. You win! Congrats!")
            break
        Guess_List.append(User_Input)
        print("\n\n")
        print(Man)
        print("\n")
        print(Guess_List)
        print("\n")
    else:
        Guess_List.append(User_Input)                # Adds guessed characters to list
        print("\nTry again!")
        Wrong_Guess += 1
        print(f"\n{6 - Wrong_Guess} wrong guesses left!\n")
        if Wrong_Guess == 1:
            Man = """|_________|
|         0
|
|
|
|"""
        elif Wrong_Guess == 2:
            Man = """|_________|
|         0
|        /
|
|
|"""
        elif Wrong_Guess == 3:
            Man = """|_________|
|         0
|        /|
|
|
|"""
        elif Wrong_Guess == 4:
            Man = """|_________|
|         0
|        /|\\
|
|
|"""
        elif Wrong_Guess == 5:
            Man = """|_________|
|         0
|        /|\\
|        /
|
|"""
        elif Wrong_Guess == 6:
            Man = """|_________|
|         0
|        /|\\
|        / \\
|
|"""
            print("Maximum number of wrong guesses met!\n")
            print(Man)
            break
        print("\n\n")
        print(Man)
        print("\n")
        print(Guess_List)
        print("\n")

print("\nGoodbye! Thanks for playing!")
