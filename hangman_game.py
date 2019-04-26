
class Hangman():
    def __init__(self):
        self.gameState = 1  # initialize state of game, 1 means on going, 0 means GAME OVER
        self.hangmanState = 6  # used to inform hangman display
        self.guessedLetters = []  # list to store guessed letters
        self.wordList = []  # list of hangman target words
        self.url = 'http://norvig.com/ngrams/sowpods.txt'  # url to for text file
        import string
        self.validLetters = list(string.ascii_uppercase)  # create a list of valid letters

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

    def setupGame(self):
        gameReady = False
        while not gameReady:
            minLength = input('Choose a minimum word length ')
            try:
                minLength = int(minLength)  # convert value into integer
            except ValueError:
                print('Please choose an integer')
            else:
                gameReady = True # no errors? then the game is ready!
        wordList = self.trimList(minLength)  # create a wordList using the minLength
        targetWord = self.pickTarget(wordList)
        return targetWord



        # while self.hangmanState > 0:  # ask for guesses anc compare until game is over
        #     guess = input('Guess a letter ')  # intake letter from
        #     if guess in self.guessedLetters:
        #         print('Already guessed this letter')
        #         self.hangmanState -= 1  # incorrect guess, decrement hangmanState
        #     else:
        #         self.guessedLetters.append(guess)  # add guess to guessed list


