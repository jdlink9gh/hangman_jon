
# import packages
import argparse
import numpy as np
import os
import random
import string

# create hangman class

class Hangman():
    def __init__(self):
        self.hangmanState = 6  # used to inform hangman display
        self.guessedLetters = []  # list to store guessed letters
        self.wordList = []  # list of hangman target words
        self.url = 'http://norvig.com/ngrams/sowpods.txt'  # url to for text file
        self.validLetters = list(string.ascii_uppercase)  # use uppercase letters for game
        self.minLength = 1  # cutoff word length for hangman game

    def checkFile (self):
        # returns the filepath of the sowpods.txt file
        # create a folder called word_data and save the file as words.txt

        fileExists = os.path.isfile('./word_data/words.txt')  # boolean to see if file exits
        if fileExists:
            return os.path.relpath('./word_data/words.txt')  # return the path of the file
        else:
            import urllib.request
            folderExists = os.path.exists('./word_data')  # check if folder exists
            if folderExists:
                textFile = urllib.request.urlretrieve(self.url, './word_data/words.txt')  # download the file
                return os.path.relpath(textFile[0])  # return the path
            else:
                os.mkdir('./word_data')  # create word_data folder
                textFile = urllib.request.urlretrieve(self.url, './word_data/words.txt')  # download the file
                return os.path.relpath(textFile[0])  # return the path

    def setupGame(self):
        filepath = self.checkFile()  # check the file to see if it exists, if not create it
        with open(filepath) as f:  # open the file and populate self.wordList
            self.wordList = [word.strip('\n') for word in f.readlines()]  # take out whitespace characters
        self.wordList = [word for word in self.wordList if len(word) >= self.minLength]  # trim using self.minLength
        target = random.choice(self.wordList)  # randomly pick a word from self.wordList
        return target

    def showBoard(self):
        print('{} remaining guesses'.format(self.hangmanState))
        print('  |‾‾‾‾|')  # print line 1 of 5
        if self.hangmanState <= 5:
            print('  |    0')  # print line 2 of 5
            if 2 <= self.hangmanState <= 4:
                if self.hangmanState == 4:
                    print('  |   / ')
                if self.hangmanState == 3:
                    print('  |   /| ')
                if self.hangmanState == 2:
                    print('  |   /|\ ')
                print('  |      ')
            if 0 <= self.hangmanState <= 1:
                print('  |   /|\ ')
                if self.hangmanState == 1:
                    print('  |   / ')
                if self.hangmanState <= 0:
                    print('  |   / \ ')
            if self.hangmanState == 5:
                print('  |    ')
                print('  |    ')
        else:
            for i in range(3):
                print('  |      ')
        print('__|__\n')  


    def showSplit(self, array):
        print(' '.join(array))  # format output for hangman

    def playGame(self):
        target = self.setupGame()  # specify target word with setupGame
        targetSplit = np.array(list(target))  # created for finding correct guesses
        maskedSplit = np.array(['_' for letter in list(target)])  # created to show state of hangman game

        while self.hangmanState > 0:
            self.showBoard()  # start off by showing state of hangman
            self.showSplit(maskedSplit)  # display state of board
            # print(target)  # used for debugging
            letterGuess = input('Guess a letter ')
            if letterGuess.upper() in self.validLetters:
                if letterGuess.upper() in self.guessedLetters:
                    self.hangmanState -= 1  # decrement for repeated guess
                    print('Already guessed this letter')
                else:
                    if letterGuess.upper() in targetSplit:
                        validSpots = np.where(targetSplit == letterGuess.upper())  # all indices of match
                        self.guessedLetters.append(letterGuess.upper())  # add guess to list of guesses
                        for index in validSpots:
                            maskedSplit[index] = letterGuess.upper()  # replace masked spot with letter
                        if '_' not in maskedSplit:
                            print('You won the game!')
                            self.showSplit(maskedSplit)  # show the completed word
                            self.showBoard()
                            self.hangmanState = -1  # exit the game since word was correctly guessed
                    else:
                        self.hangmanState -= 1  # decrement hangman state for incorrect guess
                        print('Incorrect guess')
                        self.guessedLetters.append(letterGuess.upper())
            else:
                print('Invalid input, guess a letter')
        else:
            print('Game Over!')
            self.showSplit(maskedSplit)  # show the masked split
            self.showBoard()  #  show the board
            print('Correct word was {}'.format(target))  # tell user what correct word was



def main():
    parser = argparse.ArgumentParser(description='Input a minimum word length for hangman')  # create object
    parser.add_argument("-l", '--minLength', type=int, required=True,
                        help='Minimum word length for hangman target word \n'
                             'largest value is 15 characters')  # add minLength argument
    args = parser.parse_args()  # parse the arguments

    game = Hangman()  # instantiate the class
    game.minLength = args.minLength  # set the minimum length object equal to the argument
    game.playGame()  # play the game

if __name__ == '__main__':
    main()  # call the main function
