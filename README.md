## Assignment 1 - CSC 15

Implement the BEETLE game between a player and the computer: 

* The first player to roll a dice is determined by an initial dice roll or rolls until one of the players has a higher score than the other. The player with the highest score starts the game. You can now start a game. 

* In each round of the game, the first player rolls a dice and determines if a body part can be added to its beetle. Then the second player does the same thing. 

* Repeat playing another round until one of the players has a full beetle.  

A full beetle will have one body, a head, two antennae, two eyes, 6 legs and  1 tail.   

The dice roll mapping to a body part is:

        1 – Body
        2 – Head
        3 – Legs
        4 – Eyes
        5 – Antenne
        6 – Tail

The rules for drawing the full beetle are as follows (
https://theop.games/blogs/theop/10-fun-and-easy-dice-games-to-play)

A body must be drawn before any other parts. A beetle without a body cannot have legs or a tail. Furthermore, the head must be drawn before the eyes and antenne can be added. If you roll a number associated with a body part that cannot be drawn, your turn is skipped and the next player rolls. The first player with a fully sketched beetle is the winner. 

There are two python scripts in the assignment:

* `beetle_functions.py` - contains all function definitions
* `beetle.py` - contains the code to play the game repeatedly 

Your tasks are: 

1. Complete the code of empty or unfinished functions (`beetle_functions.py`) as per the instructions written before the definition of a function in the file `beetle_functions.py`
2. Add test cases to test each function as shown at the bottom of `the beetle_functions.py` file (below the line if __ name __ == ....). 
    * Make sure that you add test cases for all possible behaviors of each function. This is very important for your grade and for making sure your game plays correctly. 
3. Test the full game by running the `beetle.py` script. 