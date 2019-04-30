import argparse
parser = argparse.ArgumentParser(description='Input a minimum word length for hangman')  # create object
parser.add_argument("-l", '--minLength', type=int, required=True,
                    help='Minimum word length for hangman target word \n'
                         'largest value is 15 characters')  # add minLength argument
args = parser.parse_args()  # parse the arguments


class Hangman():
    def __init__(self):
        self.hangmanState = 6  # used to inform hangman display
        self.guessedLetters = []  # list to store guessed letters
        self.wordList = []  # list of hangman target words
        self.url = 'http://norvig.com/ngrams/sowpods.txt'  # url to for text file
        import string
        self.validLetters = list(string.ascii_uppercase)  # use uppercase letters for game

    def checkFile (self):
        # returns the filepath of the sowpods.txt file
        # create a folder called word_data and save the file as words.txt
        import os
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

    def openFile(self):
        # opens the text file, returns raw list of words
        filepath = self.checkFile()  # call check file, which returns the relative file pile
        with open(filepath) as f:
            wordList = f.readlines()  # use readlines to create list of words
            wordList = [word.strip('\n') for word in wordList]  # take out whitespace characters
        return wordList  # return list of words

    def trimList(self, minLength):
        # minLength represents minimum string length
        self.wordList = self.openFile()  # populate wordList with openFile which
        self.wordList = [word for word in self.wordList if len(word) >= minLength]
        return self.wordList

    def pickTarget(self, wordList):
        #  select a random value from a list
        import random
        target = random.choice(wordList)  # select a random value
        return target

    def setupGame(self, minLength):
        # gameReady = False
        # while not gameReady:
        #     try:
        #         minLength = int(minLength)  # ensure
        #     except ValueError:
        #         print('Please choose an integer')
        #     else:
        #         gameReady = True  # no errors? then the game is ready!
        wordList = self.trimList(minLength)  # create a wordList using the minLength
        target = self.pickTarget(wordList)
        return target

    def showBoard(self):
        if self.hangmanState == 6:
            print('  |‾‾‾‾|')
            print('  |      ')
            print('  |      ')
            print('  |      ')
            print('__|__\n')
        if self.hangmanState == 5:
            print('  |‾‾‾‾|')
            print('  |    0')
            print('  |      ')
            print('  |      ')
            print('__|__\n')
        if self.hangmanState == 4:
            print('  |‾‾‾‾|')
            print('  |    0')
            print('  |   / ')
            print('  |      ')
            print('__|__\n')
        if self.hangmanState == 3:
            print('  |‾‾‾‾|')
            print('  |    0')
            print('  |   /| ')
            print('  |      ')
            print('__|__\n')
        if self.hangmanState == 2:
            print('  |‾‾‾‾|')
            print('  |    0')
            print('  |   /|\ ')
            print('  |      ')
            print('__|__\n')
        if self.hangmanState == 1:
            print('  |‾‾‾‾|')
            print('  |    0')
            print("  |   /|\ ")
            print('  |   / ' )
            print('__|__\n')
        if self.hangmanState <= 0:
            print('  |‾‾‾‾|')
            print('  |    0')
            print("  |   /|\ ")
            print("  |   / \ ")
            print('__|__\n')

    def showSplit(self, array):
        print(' '.join(array))  # format output for hangman

    def playGame(self, minLength):
        import numpy as np
        target = self.setupGame(minLength)  # specify target word with setupGame
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
                            break  # exit the game since word was correctly guessed
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
    game = Hangman()  # instantiate the class
    game.playGame(args.minLength)  # play the game using the argument from argparse

if __name__ == '__main__':
    main()  # call the main function
