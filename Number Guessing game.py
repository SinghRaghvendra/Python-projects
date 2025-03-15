import random

print ("Hi, Welcome to the game! \n This is a number guessing game. \n"
"You have 7 chances to guess the corect number \n Lets begin...")

range = int(input("Please enter the maximum range you want to guess: "))

guessing_number = random.randrange(range)

chances = 7

guess_count = 0

while guess_count < chances:
    guess_count += 1
    left = (chances - guess_count)

    my_guess =int(input("Please enter a number to guess: "))

    if my_guess == guessing_number:
        print(f'Congratulations! The number is {guessing_number}\n\
              and you have guessed it correctly in {guess_count} attempt.' )
        break
    elif guess_count >= chances and  my_guess != guessing_number:
        print(f'Sorry! The number is {guessing_number}. Better luck next time')

    elif my_guess > guessing_number:
        print(f'Your guess is higher than expected. {left} attempts left')
    elif my_guess < guessing_number:
        print(f'Your guess is lower than expected. {left} attempts left');



