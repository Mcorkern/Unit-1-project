
def start_game():
    num_of_guesses = 0
    import random
    solution = random.randint(1, 10)
    min_number = 1
    max_number = 10

    print(" ----------------------------------- \n•Welcome to the Number Guessing Game•\n -----------------------------------\n\nLets get this party started!")

    while True:
        try:
            number = int(input("Enter a number between 1 and 10.  "))
            num_of_guesses += 1 
        
        except ValueError:
            print("Thats not a number try again!")
        
        else: 
                if number == solution:
                    print("You did it! You guessed the number!  ")
                    break
        
                elif number < solution:
                    print("Oops, the number is higher. Try again.  ")
                    continue
                
                elif number < min_number or number > max_number:
                    print("That number isn't between 1 and 10, try again.")
                    continue
                
                elif number > solution:
                    print("Opps, the number is lower. Try again.  ")
                    continue
    
    print("Amazing it took you {} guesses to get it right! The high score is...".format(num_of_guesses))
    ### still trying to figure out how to store and show the high score 
    while True:
        print("Would you like to play again? Yes/No  ")
        play_again = input("")
    
        if play_again.lower() == "no":
            print("Thanks for playing! See you next time!")
            break
    
        elif play_again.lower() == "yes":
            start_game() 
            continue
                
start_game()



