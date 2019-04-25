# hangman_jon
For this exercise, we wil be using, github, markdown and python to create a hangman game.
### Steps
Here are the steps you will need to follow:
1) Create a new branch off of the 'development' branch of your repository.
2) Create your hangman game using a class called 'Hangman'
    - This class may have many member variables and functions to accomplish your task 
3) Define a "main" function to drive your game
4) Call main by using the the code:
```
if __name__ == "__main__":
    main()
```
5) Create a readme file using markdown to describe how your game works
    - include a description of your code
    - include any inputs or outputs you may use along with their descriptions
    - include a description of how to operate/call your game
6) Please add and commit your code (using the -m flag to provide a description) periodically to keep track of your 
status. Please push your code at milestones. You can push multiple commits at the same time.
7) Once your code is ready for review, please initiate a merge request of your branch back into development. Assign Jack
Linkous (jdlink9gh) as the reviewer.

### Inputs and Outputs
#### Inputs
- The function should take in a parameter from the command line using the 'argparse' module
- This input should be the minimum length of word you would like to guess during your game
- Please use a description to provide the user general information on you program as well as the help variable on your 
 arguments to provide info on the particular flags. This information will be displayed if the user uses the '-h' flag.
#### Outputs
- The only output to this program will be if there is no locally stored word file. we will discuss how this word file is 
obtained below, but if the file does not exists please have your code create a folder called 'word_data' and store the
file as words.txt.
- Be sure this file is not uploaded to the git repo, as we do not want to add anything to our repo besides code.
### Hangman
- This code will operate a game of hangman.
- The code will first check to see if a file is stored locally and open it.
- If not it will go up to http://norvig.com/ngrams/sowpods.txt and download the data.
- You code should then parse this data into a list and store the data in the aforementioned location.
- The program will then choose a word at random that is at least as long as the minimum length specified by the input 
argument.
- The code will loop until the word is either guessed correctly or the player has run of body parts.
- The loop will display:
    - The current state of the hangman
    - The current state of the word, with '_' used as unguessed letters
    - The letters available to choose
    - Ask the user to choose a letter
    - Notify the user if the letter is in the word, if it is not in the word, if the user has already guessed the
    letter, if the input is more than one character, or if the chosen value is not a letter
    - If the letter is wrong, or it has already been guessed, update the hangman, and restart the loop
    - If the value is not a letter, or if the value is more than one character, do not penalize the user, but restart the loop
    - If the letter is correct, update the guess and restart the loop 
- A full hangman (a loss) will display as (use this as a guide):
```
|‾‾‾‾‾‾‾|
|       O
|      /|\
|      / \
|
```
- Upon the end of the game, notify the user what the word was and tell them whether they won or lost