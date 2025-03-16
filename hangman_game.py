print("Welcome to Hangman Game!")

import random
from collections import Counter

wordbank = ''' apple mango orange grapes payapaya coconut
banana guava lemon strawberry watermelon cherry papaya'''

word = wordbank.split()

#Need to choose a random word from the wordbank that needs to be guessed
word = random.choice(word)



if __name__ == '__main__':
    print("Guess the word. the word is name of a fruit.")

    for i in word:
        print("*", end = "") #for printing spaces of the word letters
    print()

    playing = True

    lettersguessed = '' #stores the letters guessed by the player
    chances = len(word) +2
    correct = 0
    flag = 0
    try:
        while (chances != 0) and flag == 0:
             #flag is updated when the word is correctly guessed
             print()
             chances -= 1

             try:
                 guess = str(input("Enter a letter to guess:"))
             except:
                print("Enter only a letter")
                continue
             #Validation of guess
             if not guess.isalpha():
                 print("Enter only a Letter")
                 continue
             elif len(guess)>1:
                 print("Enter only a single letter")
                 continue
             elif guess in lettersguessed:
                 print("You have already guessed that Letter")
                 continue
             
             #If the letter is guessed correctly

             if guess in word:
                 #K will store the number of times guessed letter occurs in word
                  k = word.count(guess)
                  for _ in range(k):
                        lettersguessed += guess #guess letter is added as many times as it occurs

                        # Print the word
             for char in word:
                if char in lettersguessed and (Counter(lettersguessed) != Counter(word)):
                    print(char, end=' ')
                    correct += 1
                # If user has guessed all the letters
                # Once the correct word is guessed fully,
                elif (Counter(lettersguessed) == Counter(word)):
                    # the game ends, even if chances remain
                    print("The word is: ", end=' ')
                    print(word)
                    flag = 1
                    print('Congratulations, You won!')
                    break  # To break out of the for loop
                    break  # To break out of the while loop
                else:
                    print('_', end=' ')

        # If user has used all of his chances
        if chances <= 0 and (Counter(lettersguessed) != Counter(word)):
            print()
            print('You lost! Try again..')
            print('The word was {}'.format(word))

    except KeyboardInterrupt:
        print()
        print('Bye! Try again.')
        exit()


  
  
