# Tic-tac-toe

Part of the Data Analyst bootcamp was the task to write a working Python script that allows two people to play tic-tac-toe against each other. Instead of writing one big function that does everything, we had to split the game into several, smaller functions, each for a specific task.

### Step 1: Getting started
Let's start with the main structure, which will start your game when you run the script name in the command line. If you have a look into the tic_tac_toe.py file you will see that the first line is already there. Inside this structure you can call all the other functions to perform their tasks. 

Since a game of Tic-tac-toe is basically repeating the same tasks over and over again (like asking the players for input) a `while true` loop can help you to get the game running. You have to make sure, however, that in case of certain events (win, draw,...) the loop will break so that the game will come to an end.
Another challenge to think about is how to allow each player to take turns at making their moves. Here the `modulo` operator could be helpful.

### Step 2: Display the board 
To play a round of tic-tac-toe, we need a game board. We should start by defining a function that will display the board on the screen when it is called. There are several ways to display a tic-tac-toe board. Choose the implementation that you can work best with as we proceed.

### Step 3: Choose a symbol  
Before we can start playing it would be nice if the first player can choose whether to play with "X" or "O"! Player two must then choose the other.

### Step 4: Ask for player input 
Now you need a function that asks the player (whose turn it is) where he wants to put his marker. The built-in function `input()` will do this task for you. 
If you want, you can directly add a control mechanism that checks if the desired position was already occupied in a previous turn. 

### Step 5: Check for Winner
At the end of each turn, your script will have to determine if the most recent play resulted in a win. If it did, it should break the game loop, the player that just played will be declared the winner, the game will be over, and the script will terminate. If a winner is not found, play will continue.
Keep in mind that there are 8 different ways for a player to get three in a row. The function you write to solve this part of the problem will have to implement a lot of logic. Hint: One way to potentially make this part less code-intensive is by using the built-in function `all()`.

### Step 6: Check for Draw
There is a distinct chance that a draw will occur in the game. If this happens, your script should be aware. If all of the squares have been filled in, and there is no winner, it should break the game loop and a draw should be declared.
