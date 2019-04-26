
class Hangman():
    def __init__(self):
        self.gameState = 1  # initialize state of game, 1 means on going, 0 means GAME OVER BITCH
        self.hangmanState = 6  # used to inform hangman display
        self.guessedLetters = []  # list to store guessed letters
        self.url = 'http://norvig.com/ngrams/sowpods.txt'  # url to for text file

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

