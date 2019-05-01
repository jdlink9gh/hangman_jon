# hangman_jon

### Overview
Hangman is a game where a user will attempt to guess a 'masked' word letter by letter. For each correct guess, all the
spots with a match are revealed. For each incorrect guess, a 'body part' is added to the hangman. The game is complete
when either of the following conditions are met: 

1. The user has correctly guessed the word and no hidden characters are left 
2. The user has exhausted all their guesses and a full hangman is shown 

### Calling the game
Users call the game from the command line by entering the directory of the hangman_game.py file. Then, enter the
following command: hangman_game.py -l integer

If the user needs help, they can use the following command: hangman_game.py -h

### Structure of the Code

Hangman is defined as a class within the code with various objects and methods. A quick explanation of each is below.

#### Objects
- self.hangmanState: integer, denotes how many incorrect guesses a user is allowed, once it reaches 0 the user loses
- self.guessedLetters: list, stores the guessed letters within the game, initialized as an empty list
- self.wordList: list, list of target words for hangman game 
- self.url = str, 'http://norvig.com/ngrams/sowpods.txt' is the url which stores a text file
- self.validLetters = list, list of uppercase letters which represent valid guesses  

#### Methods
- __init__(self): initializes the class with the objects above 
- checkFile(self): returns the filepath of a downloaded text file, if the file is not present, download the file
- setupGame(self): returns the word to be guessed (target word) by: 
    - Calling checkFile to obtain a file path
    - Opening the file and converting it into a list
    - Trimming the list to words that have length >= self.minLength
    - Selecting a word from the trimmed at random 
- showBoard(self): prints the hangman board according to the self.hangmanState
- showSplit(self, array): joins an array with spaces in between, used to format the target word and guessed letters
- playGame(self): logic for the hangman game, calls the setupGame method to pick a target word
    - The playGame(self) method also creates an array of the target word as well as a masked array, which is simply
        each letter replaced by an underscore 
    - Users are prompted to guess a letter, which is checked to see if it has been previously guessed and if the 
        letter is in the target word 
    - If the letter is within the word and not a repeated guess, the masked array's underscores are replaced by the 
        letter and the user is prompted for another letter 
    - If the letter has already been guessed or it is not in the target word, the user is 'penalized' with a body 
        part 'drawn' on the hangman and the user is prompted for another letter
    - This process repeats until either of the conditions in the overview section are met
- main(): used to drive the hangman game, when the file is called from the command line, main instantiates 
    the Hangman class and sets the self.minLength object to value entered from the user using the argparse module 