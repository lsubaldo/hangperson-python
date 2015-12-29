import random

def printGallows(num_missed):
    '''
    (int) -> None

    Print a representation of the hangperson gallows.  The parameter
    to the function is the number of missed words.  7 misses means
    that the player has lost (and the full gallows gets printed).
    '''
    if (num_missed < 0 or num_missed > 7):
        raise Exception("Invalid number of missed words when attempting to print the gallows.")


    print 
    print 
    print '       |||========|||'
    if num_missed > 0:
        print '       |||         |'
    else:
        print '       |||          '

    if num_missed > 1:
        print '       |||         O'
    else:
        print '       |||          '

    if num_missed > 2:

        if num_missed > 4:
            print '       |||        /|\\'
        elif num_missed > 3:
            print '       |||        /| '
        else:
            print '       |||        /  '
    else:
        print '       |||           '

    if num_missed > 5:
        if num_missed > 6:
            print '       |||        / \\'
        else:
            print '       |||        /  '
    else:
        print '       |||           '

    print '       |||'
    print '       |||'
    print '     ================='
    print  

def secret_word():
    '''
    () -> NoneType
    Returns a randomly chosen word from the list, wordlist.
    '''
    wordlist = ['HAMILTON', 'GRASS','COLGATE', 'FALL', 'WINTER', 'WIND', 'SNOW', 'COLD', 'DEER', 'RAIDER', 'MAROON', 'WHITE']
    secretword = random.choice(wordlist)
    return secretword

def check_letter(letter):
    '''
    (str) -> bool
    Verifies that input is a single letter. Returns True if it is.
    Returns False otherwise.
    >>>check_letter('aaaa')
    You can only type a single letter...
    False
    >>>check_letter(9)
    Come on, you have to type a letter.
    False
    >>>check_letter(49ers)
    Come on, you have to type a letter.
    False
    >>>check_letter('p')
    True
    '''
    if len(letter) < 1:
        print "You didn't type anything. I can't read minds!"
        return False
    elif len(letter) > 1 and not letter.isalpha():
        print "Come on, you have to type a letter."
        return False
    elif len(letter) > 1:
        print "You can only type a single letter..."
        return False
    elif not letter.isalpha():
        print "Come on, you have to type a letter."
        return False
    else:
        return True

def guess_letter(guess_num):
    '''
    () -> NoneType
    Prompts user for acceptable guess. Guess is acceptable if
    it is a single letter.

    Returns uppercase version of guessed letter. 
    '''
    prompt = "Guess a letter: "
    letter = raw_input(prompt)
    while not check_letter(letter):
        letter = raw_input(prompt)
    return letter.upper()


def in_word(secretword, letter, correct_letters):
    '''
    (str, str, list of str) -> list of str
    If letter is in secretword at index i, it will update
    the list of str, correct_letters, at that index i.
    Returns the list of str. 
    '''
    i = 0
    while i < len(secretword):
        if secretword[i] == letter:
            correct_letters[i] = letter
        i += 1
    return correct_letters
    

def play_game():
    '''
    () -> NoneType
    Plays a single game of Hangperson.
    '''
    secretword = secret_word()
    max_guesses = 7
    num_guesses = 0
    letters_guessed = []
    correct_letters = ['__'] * len(secretword)  #where the letters of 
    printGallows(num_guesses)                   #secretword will go when guessed
    print ' '.join(correct_letters)
    while num_guesses < max_guesses:            
        guess = guess_letter(num_guesses)
        while guess in letters_guessed:    #checking if letter that was guessed was guessed already
            print "Silly you. You already guessed that letter."
            guess = guess_letter(num_guesses)
        if guess in secretword:
            correct_letters = in_word(secretword, guess, correct_letters)  #updating list
            if correct_letters == list(secretword):      #win!
                print "Congratulations! You guessed the secret word, " + secretword + "!"
                break
            else:
                printGallows(num_guesses)           #will not update gallow
        else:
            num_guesses += 1
            printGallows(num_guesses)             #will print with additional gallow
            if num_guesses == max_guesses:              #lost
                print "Sorry, the secret word was " + secretword
        letters_guessed += [guess]                #accumulating the letters that have been guessed
        print "Previous guesses: " + ' '.join(letters_guessed) 
        print ' '.join(correct_letters)     
               

def main():
    '''
    () -> NoneType
    Plays as many games of Hangperson as the user wants. Asks user after
    each game if they want to play again. 
    '''
    print "Welcome to Hangperson! Can YOU guess the secret word?"
    keep_playing = True
    while keep_playing:
        play_game()
        keep_playing = raw_input("Play again? (y for yes) ") == 'y'
    print "Thanks for playing!" 


main()
