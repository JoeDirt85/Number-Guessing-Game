import random

def welcome_display():  #Fucntion with welcome display and instructions for the game
    print('Welcome to the number guessing game. ')
    print('You must guess a number between 1 and 100. ')
    print('You have x number of guesses to win the game. ')
    print('-' * 45)

def difficulty_selection(): #Display for different difficulties
    print('Please select your difficulty. ')
    print('Easy: 10 guesses. ')
    print('Medium: 5 guesses. ')
    print('Hard: 3 guesses. ')
    print('-' * 30)

    while True: #Loop for difficulty selection, Easy, Medium and Hard options
        difficulty = input('Enter your difficulty.').lower()
        if difficulty == 'easy':
            attempts = 10
            break
        elif difficulty == 'medium':
            attempts = 5
            break
        elif difficulty == 'hard':
            attempts = 3
            break
        else:
            print('That is not a valid option, please select: Easy, Medium or Hard.')

    print(f'You have selected {difficulty} difficulty, you will get {attempts} attempts.')
    return attempts

def number_to_guess(): #selects the random number of the game to guess
    return random.randint(1, 100)

def gameplay(): #Gameplay function, calls difficulty and random number function
    attempts = difficulty_selection()
    random_number = number_to_guess()
    guesses = 0

    while guesses < attempts: #loop to check if number of guesses is below allowed attempts
        print(f'You have made {guesses} guesses. You have {attempts - guesses} left.')
        player_guess = int(input('Please enter a number.'))

        if 1 <= player_guess <= 100: #Loop to check if player input is within the required range
            if player_guess == random_number: #Loop for gameplay, informs player if they are high or low
                print(f'Congratulations! You got it right! It took you {guesses} guesses to get the right number.')
                return
            elif player_guess < random_number:
                print(f'{player_guess} was too low, guess again.')
                guesses = guesses + 1
            elif player_guess > random_number:
                print(f'{player_guess} was too high, guess again.')
                guesses = guesses + 1

        else:
            print('Input was out of range. Please enter a number between 1 and 100.')

    print("You ran out of guesses, you lose!")


def main(): #main function to run the game
    welcome_display()
    gameplay()

if __name__ == '__main__':
    main()
