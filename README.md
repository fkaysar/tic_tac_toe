# Tic-tac-toe

Part of the Data Analyst bootcamp was the task to write a working Python script that allows two people to play tic-tac-toe against each other. Instead of writing one big function that does everything, we had to split the game into several, smaller functions, each for a specific task.

### Step 1: Getting started
Let's start with the main structure, which will start your game when you run the script name in the command line. If you have a look into the tic_tac_toe.py file you will see that the first line is already there. Inside this structure you can call all the other functions to perform their tasks. 

Since a game of Tic-tac-toe is basically repeating the same tasks over and over again (like asking the players for input) a `while True` loop can help you to get the game running. You have to make sure, however, that in case of certain events (win, draw,...) the loop will break so that the game will come to an end.
Another challenge to think about is how to allow each player to take turns at making their moves. Here the `modulo` operator could be helpful.

## Step 2
