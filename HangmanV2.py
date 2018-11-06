import random
import os
clear = lambda: os.system('cls')
Word_List = list(range(1,2997))
inFile = open('Hangman_Answers.txt', 'r')
counter = 0
times_played = 0
repeat = ""
User_Input = ""
Word_List.append("Placeholder")
for line in inFile:
    Word_List[counter] = line #Populates the list
    counter += 1
User_Name = input("Hello user! Please enter your name so I can refer to you properly. :]\n") #Gets the user name to refer to later
print(f"\n\nThank you {User_Name}, and without further ado...\n\n")
print("Welcome to..........")
print("""
 ▄         ▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄        ▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄       ▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄        ▄  ▄
▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░░▌      ▐░▌▐░░░░░░░░░░░▌▐░░▌     ▐░░▌▐░░░░░░░░░░░▌▐░░▌      ▐░▌▐░▌
▐░▌       ▐░▌▐░█▀▀▀▀▀▀▀█░▌▐░▌░▌     ▐░▌▐░█▀▀▀▀▀▀▀▀▀ ▐░▌░▌   ▐░▐░▌▐░█▀▀▀▀▀▀▀█░▌▐░▌░▌     ▐░▌▐░▌
▐░▌       ▐░▌▐░▌       ▐░▌▐░▌▐░▌    ▐░▌▐░▌          ▐░▌▐░▌ ▐░▌▐░▌▐░▌       ▐░▌▐░▌▐░▌    ▐░▌▐░▌
▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌▐░▌ ▐░▌   ▐░▌▐░▌ ▄▄▄▄▄▄▄▄ ▐░▌ ▐░▐░▌ ▐░▌▐░█▄▄▄▄▄▄▄█░▌▐░▌ ▐░▌   ▐░▌▐░▌
▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌  ▐░▌  ▐░▌▐░▌▐░░░░░░░░▌▐░▌  ▐░▌  ▐░▌▐░░░░░░░░░░░▌▐░▌  ▐░▌  ▐░▌▐░▌
▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌▐░▌   ▐░▌ ▐░▌▐░▌ ▀▀▀▀▀▀█░▌▐░▌   ▀   ▐░▌▐░█▀▀▀▀▀▀▀█░▌▐░▌   ▐░▌ ▐░▌▐░▌
▐░▌       ▐░▌▐░▌       ▐░▌▐░▌    ▐░▌▐░▌▐░▌       ▐░▌▐░▌       ▐░▌▐░▌       ▐░▌▐░▌    ▐░▌▐░▌ ▀
▐░▌       ▐░▌▐░▌       ▐░▌▐░▌     ▐░▐░▌▐░█▄▄▄▄▄▄▄█░▌▐░▌       ▐░▌▐░▌       ▐░▌▐░▌     ▐░▐░▌ ▄
▐░▌       ▐░▌▐░▌       ▐░▌▐░▌      ▐░░▌▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░▌       ▐░▌▐░▌      ▐░░▌▐░▌
 ▀         ▀  ▀         ▀  ▀        ▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀         ▀  ▀         ▀  ▀        ▀▀  ▀
""")
repeat = input("Would you like to play? y/n\n") #Origin to loop
while repeat != "n":
    Wrong_Guess = 0
    Guess_List = []
    Guess_List.append("Letters used:") #Creates guess list
    Hint_Enable = input("Would you like to play with hints? y/n\n") # asks about hints
    Clear_Enable = input("Would you like to clear the screen after each turn? y/n\n") #asks about clearing screen
    if times_played > 0 and Clear_Enable == 1:
        clear()
    print("\nWelcome to Hangman! type quit at any time to exit the game, enter a lowercase letter to guess, or guess the word.\n")
    Man = """|_________|
|
|
|
|
|"""
    Original_Word = Word_List[random.randint(1,2997)] #Selects a random word
    Original_Word = Original_Word.replace("\n","")
    Current_Guess = "-" * len(Original_Word)
    while Original_Word != Current_Guess and User_Input != "quit":   # if still not complete, or user does not choose to quit
        print(Current_Guess)
        Hint_Num = random.randint(0,len(Original_Word) - 1)
        User_Input = input("\nEnter a character, or guess the word: ")
        if User_Input in Original_Word and User_Input not in Guess_List: #Checks to make sure the character isn't used before
            if User_Input != Original_Word:
                clear()
                print(f"\nYes! {User_Input}, is in the word!") #positive response
                new = ""
                for i in range(len(Original_Word)):
                    if User_Input == Original_Word[i]:
                        new += User_Input                # fill the position with new value
                    else:
                        new += Current_Guess[i]           # same value as before
                Current_Guess = new
            else:
                if Clear_Enable == "y":
                    clear()
                print(f"\nYes! {User_Input}, is the word!")
            if Original_Word == Current_Guess or User_Input == Original_Word:
                print("""
 ▄         ▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄         ▄       ▄         ▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄        ▄  ▄
▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░▌       ▐░▌     ▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░░▌      ▐░▌▐░▌
▐░▌       ▐░▌▐░█▀▀▀▀▀▀▀█░▌▐░▌       ▐░▌     ▐░▌       ▐░▌ ▀▀▀▀█░█▀▀▀▀ ▐░▌░▌     ▐░▌▐░▌
▐░▌       ▐░▌▐░▌       ▐░▌▐░▌       ▐░▌     ▐░▌       ▐░▌     ▐░▌     ▐░▌▐░▌    ▐░▌▐░▌
▐░█▄▄▄▄▄▄▄█░▌▐░▌       ▐░▌▐░▌       ▐░▌     ▐░▌   ▄   ▐░▌     ▐░▌     ▐░▌ ▐░▌   ▐░▌▐░▌
▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░▌       ▐░▌     ▐░▌  ▐░▌  ▐░▌     ▐░▌     ▐░▌  ▐░▌  ▐░▌▐░▌
 ▀▀▀▀█░█▀▀▀▀ ▐░▌       ▐░▌▐░▌       ▐░▌     ▐░▌ ▐░▌░▌ ▐░▌     ▐░▌     ▐░▌   ▐░▌ ▐░▌▐░▌
     ▐░▌     ▐░▌       ▐░▌▐░▌       ▐░▌     ▐░▌▐░▌ ▐░▌▐░▌     ▐░▌     ▐░▌    ▐░▌▐░▌ ▀
     ▐░▌     ▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌     ▐░▌░▌   ▐░▐░▌ ▄▄▄▄█░█▄▄▄▄ ▐░▌     ▐░▐░▌ ▄
     ▐░▌     ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌     ▐░░▌     ▐░░▌▐░░░░░░░░░░░▌▐░▌      ▐░░▌▐░▌
      ▀       ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀       ▀▀       ▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀        ▀▀  ▀

""")
                print(f"\nThe word was: {Original_Word}. Congrats, {User_Name}!\n")
                break
            Guess_List.append(User_Input)
            print("\n\n")
            print(Man)
            print("\n")
            print(Guess_List)
            print("\n")
        else:
            if User_Input not in Guess_List:
                Guess_List.append(User_Input) # Adds guessed characters to list
            else:
                print(f"\nYou already used that character, and now you've lost a guess {User_Name}!")
            Wrong_Guess += 1
            if Clear_Enable == "y":
                clear()
            if Wrong_Guess <= 5:
                print("\nTry again!\n")
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
                if Current_Guess[Hint_Num] == "-" and Hint_Enable == "y":
                    print("*" * 20)
                    print(f"\nHint: one of the letters is {Original_Word[Hint_Num]}!\n")
                    print("*" * 20)
            elif Wrong_Guess == 4:
                Man = """|_________|
|         0
|        /|\\
|
|
|"""
                if Current_Guess[Hint_Num] == "-" and Hint_Enable == "y":
                    print("*" * 20)
                    print(f"\nHint: one of the letters is {Original_Word[Hint_Num]}!\n")
                    print("*" * 20)
            elif Wrong_Guess == 5:
                Man = """|_________|
|         0
|        /|\\
|        /
|
|"""
                if Current_Guess[Hint_Num] == "-" and Hint_Enable == "y":
                    print("*" * 20)
                    print(f"\nHint: one of the letters is {Original_Word[Hint_Num]}!\n")
                    print("*" * 20)
            elif Wrong_Guess == 6:
                Man = """|_________|
|         0
|        /|\\
|        / \\
|
|"""
                if Clear_Enable == "y":
                    print("""
 ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄       ▄▄  ▄▄▄▄▄▄▄▄▄▄▄       ▄▄▄▄▄▄▄▄▄▄▄  ▄               ▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄
▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░▌     ▐░░▌▐░░░░░░░░░░░▌     ▐░░░░░░░░░░░▌▐░▌             ▐░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌
▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌▐░▌░▌   ▐░▐░▌▐░█▀▀▀▀▀▀▀▀▀      ▐░█▀▀▀▀▀▀▀█░▌ ▐░▌           ▐░▌ ▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌▐░▌
▐░▌          ▐░▌       ▐░▌▐░▌▐░▌ ▐░▌▐░▌▐░▌               ▐░▌       ▐░▌  ▐░▌         ▐░▌  ▐░▌          ▐░▌       ▐░▌▐░▌
▐░▌ ▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄█░▌▐░▌ ▐░▐░▌ ▐░▌▐░█▄▄▄▄▄▄▄▄▄      ▐░▌       ▐░▌   ▐░▌       ▐░▌   ▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄█░▌▐░▌
▐░▌▐░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌  ▐░▌  ▐░▌▐░░░░░░░░░░░▌     ▐░▌       ▐░▌    ▐░▌     ▐░▌    ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌
▐░▌ ▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌▐░▌   ▀   ▐░▌▐░█▀▀▀▀▀▀▀▀▀      ▐░▌       ▐░▌     ▐░▌   ▐░▌     ▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀█░█▀▀ ▐░▌
▐░▌       ▐░▌▐░▌       ▐░▌▐░▌       ▐░▌▐░▌               ▐░▌       ▐░▌      ▐░▌ ▐░▌      ▐░▌          ▐░▌     ▐░▌   ▀
▐░█▄▄▄▄▄▄▄█░▌▐░▌       ▐░▌▐░▌       ▐░▌▐░█▄▄▄▄▄▄▄▄▄      ▐░█▄▄▄▄▄▄▄█░▌       ▐░▐░▌       ▐░█▄▄▄▄▄▄▄▄▄ ▐░▌      ▐░▌  ▄
▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░▌       ▐░▌▐░░░░░░░░░░░▌     ▐░░░░░░░░░░░▌        ▐░▌        ▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░▌
 ▀▀▀▀▀▀▀▀▀▀▀  ▀         ▀  ▀         ▀  ▀▀▀▀▀▀▀▀▀▀▀       ▀▀▀▀▀▀▀▀▀▀▀          ▀          ▀▀▀▀▀▀▀▀▀▀▀  ▀         ▀  ▀
""")
                print("\n\n")
                print(Man)
                print("\n\n")
                print(f"Maximum number of wrong guesses met! The word was {Original_Word}.\n")
                break
            print(f"\n{6 - Wrong_Guess} wrong guesses left!\n")
            print("\n\n")
            print(Man)
            print("\n")
            print(Guess_List)
            print("\n")
    times_played += 1
    repeat = input(f"{User_Name}, Would you like to play again? y/n\n")
print(f"\nGoodbye! Thanks for playing {User_Name}!")
