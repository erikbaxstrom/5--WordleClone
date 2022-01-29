# A word guessing game cloned from Wordle

import random

# Dictionary of words
dictionary = ['perky'] # yes, the dictionary only has one word in it. 

# display game instructions
print('Welcome to WordleClone')
print('I am thinking of a five letter word.')
print('After each guess, you get feedback')
print('X means the letter was in the word and in the correct spot')
print('x means the letter was in the word but in the wrong spot')
print('- means the letter was not in the word')
print('You have six guesses. Good luck!')

keepPlaying = True
while keepPlaying: # main loop of game
    # randomly choose a word
    secretWord = dictionary[ random.randint(0,len(dictionary)-1) ] # choose a word from the dictionary randomly

    # guessing loop
    guessCount = 1
    win = False
    feedback = list('-----') # start with a list of '-'
    while guessCount <=6 and win == False:
        # ask for a guess
        print('what is your guess?')
        guess = input()
        # Check the letters in the guess against the secretWord and provide feedback
        try:
            for i in range(5):
                if guess[i] == secretWord[i]: # is the letter in the correct position?
                    feedback[i] = 'X'
                elif guess[i] in secretWord: # is the letter in the word?
                    feedback[i] = 'x'
                else: # letter is not in the word.
                    feedback[i] = '-'
            print(''.join(feedback)) #provide the feedback to the user. join the list w/ no character separator so we can print it as a string. 
        except: # if we fail for any reason, assume the guess is invalid. 
            print('invalid guess')
        # check if game has been won
        if guess == secretWord:
            print('Yay! You took', guessCount, 'guesses.')
            win = True
        else: # game has not been won
            guessCount += 1
        if guessCount > 6:
            print('you failed')
    # Check if user wants to play again
    choice = ''
    while choice not in ['y','n']: #only accept 'y' or 'n' as user input
        print('play again? [y/n]')
        choice = input()
    if choice == 'n': # user wants to quit
        print('Thank you for playing. Goodbye!')
        keepPlaying = True
        break
    elif choice == 'y': # user wants to keep playing
        # reset the game
        guessCount = 1
        win = False
        print('Im thinking of a new word.')
        
