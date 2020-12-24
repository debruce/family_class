from random_word import RandomWords
r = RandomWords()

#Return a single random word
guessing = r.get_random_word()
 

print('''
Welcome to Hangman!
This is an English word guessing game, where
the player chooses letters in an attempt to
guess what the randomly provided word is.
''')
print("Guess the characters:")

guesses = ''
turns = 17

while turns > 0:

    failed = 0
    for char in guessing: 
        if char in guesses: 
            print(char)
        else: 
            print("_")
            failed += 1
             
    if failed == 0:
        print("You won! The word is: ", guessing) 
        restart = input("Would you like to play again? Y/N:")
        if restart == 'y' or 'Y':
            continue
        elif restart == 'n' or 'N':
            break
        else:
                print("Invalid input.")
     
    guess = input("Guess a character:")
    guesses += guess 
     
    if guess not in guessing:
        turns -= 1
        print("Wrong, You have", + turns, "more guesses.")   
        if turns == 0:
            print("You lost.")
            restart = input("Would you like to play again? Y/N:")
            if restart == 'y' or 'Y':
                continue
            elif restart == 'n' or 'N':
                break
            else:
                print("Invalid input.")
