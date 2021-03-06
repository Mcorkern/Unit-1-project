#### I am trying for all of the "Exceeds expectations" but would be happy with the "meets expectations" 
#### as long as I could get some notes on where I went wrong if possible. 

current_high_score = 10
def get_high_score():
    global current_high_score
    
    if num_of_guesses < current_high_score:
        current_high_score = num_of_guesses
        print("Amazing it took you {} guesses to get it right! The new high score is {}!".format(num_of_guesses, current_high_score))
        
    elif num_of_guesses > current_high_score: 
        print("Awesome it took you {} guesses to get it right! But the high score is {}. Maybe next time you can beat it.".format(num_of_guesses, current_high_score))
    elif current_high_score == 1 and num_of_guesses == current_high_score:
        print("You nailed it and got it in 1 try! You have the best high score possiple at {} attempt! ". format(current_high_score))  
    else:
        print("Nice it took you {} guesses to get it right this time but the high score is {}. Can you beat that? Let's find out!".format(num_of_guesses, current_high_score))        
    return current_high_score
        
def play_again():
    play_again = True
    while play_again:
                
        print("Would you like to play again? Yes/No  ")
        play_again = input("") 
            
        if play_again.lower() == "no":
            print("Thanks for playing! See you next time!")
            break
    
        elif play_again.lower() == "yes":
            start_game() 
            continue

def start_game():
    
    global num_of_guesses 
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
                get_high_score()
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
    
            
    
    


start_game()
play_again()

