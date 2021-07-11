# 3 digit guessing game
import random
num_digits = 3
max_guesses = 10

def main():
    print(f'''Bagels is a 3 digit logic game where the player must guess a three digit number.
    I'm thinking of a {num_digits}-digit number with no repeated digits, can you guess what it is?
    Hint: When I say,
    Pico: One digit is correct but in the wrong position
    Fermi: One digit is correct and in the correct position
    Bagels: No digits are correct. 
    For example, if the number is 248 and the guess was 843, the clue will be Fermi Pico.''')
    while True:
        secretNum = getSecretNumber()
        print('I have thought of a number.')
        print(f'You have {max_guesses} guesses to get it.')
        num_guesses = 1
        while num_guesses <= max_guesses:
            guess  = ''
            while len(guess) != num_digits or not guess.isdecimal():
                print(f'Guess # {num_guesses}: ')
                guess = input('> ')
            clues = getClues(guess, secretNum)
            print(clues)
            num_guesses += 1

            if guess == secretNum:
                break
            if num_guesses > max_guesses:
                print(f'You ran out of guesses. The number was {secretNum}')
        print('Do you want to play again? (yes or no)')
        if not input('> ').lower().startswith('y'):
            break
    print('Thanks for playing!')

def getSecretNumber():
    ### randomize a secret number.
    numbers = list(range(10))
    random.shuffle(numbers)
    secretNum = ''
    for i in range(num_digits):
        secretNum += str(numbers[i])
    return secretNum

def getClues(guess, secretNum):
    ### return Fermi if digit is correct and in place, Pico is digit is correct but not in place, otherwise return Bagels.
    if guess == secretNum:
        return 'You got it!'

    clues = []

    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            clues.append('Fermi')
        elif guess[i] in secretNum:
            clues.append('Pico')
    if len(clues) == 0:
        return 'Bagels'
    else:
        clues.sort()
        return ' '.join(clues)

if __name__ == '__main__': # If the program is run (instead of imported), run the game
    main()