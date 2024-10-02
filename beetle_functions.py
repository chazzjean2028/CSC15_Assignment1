'''
    This python program implements the functions for playing the BEETLE game 
    between a player and the computer

    Author: ADD YOUR NAME HERE
    Date:   ADD THE DATE COMPLETED HERE

'''

# import statements 
import random 
import time 

# global variables - assigned outside any function, can be accessed in any function, but not changed
# maps a dice value to a body part 
dict_dice2body = {1:'body', 2:'head', 3:'leg', 4:'eye', 5:'antenna', 6: 'tail'}
# defines the number of body parts needed for a full beetle
dict_full_body = {'body':1, 'head':1, 'leg':1, 'eye':1, 'antenna':1, 'tail':1}

# function definitions
''' 1. TO DO
    Function: check_add_part
    Purpose: checks if a dice roll corresponds to a body part that can be added to current body
    Input parameters: body - a dictionary with the body parts so far for a player
                      dice_roll - the dice face rolled by a player
    Processing: 
       1. find body part given the dice_roll (use dict_dice2body)
       2. if the body part already exists 
            print message to "You already habe a ", returnm False
       3. add = False # this is a variable you will return at the end of the function 
       4. message = '' # this will hold a descriptive message to print for the player before the function ends
       5. check conditions to add that body part:
                if Head or Body - set result to True
                if eyes or antennae
                  if Head is there, then set add to True
                  else set message: "You cannot add ", part, "because you don't have a head yet"
                if legs or tail 
                    if body is there, then set add to True
                    else set message: "You cannot add ", part, "because you don't have a body yet"
       6. If add is True print: "You can add ", part, "to your body". 
          else: print message set in step 4
       7. Return add
    Precondition: dice_roll is an integer number between 1 and 6
'''
def check_add_part(body, dice_roll):
    assert(dice_roll >=1 and dice_roll <=6)

    # ADD CODE HERE to check if the body part can be added
    add = False
    return add

''' 2. TO DO 
    Function: add_part
    Purpose: add a body part to the beetle
    Input parameters: body - a dictionary with a player's beetle body
                      dice_roll - the dice face rolled by a player
    Processing: 
        1. find the body part for the roll
        2. set to 1 to the value of that body part key in the body dictionary 
        3. return body
    Return: the updated body dictionary
    Preconditions: 
        - The part CAN BE ADDED to the body (check_add_part() was called before add_part()
        and returned True), 
        - the value of the body part you want to add is 0. If it already 1, you have a mistake
        - dice_roll is an integer number between 1 and 6
    Postcondition: body dictionary has changed the value of one key from 0 to 1.
'''
def add_part(body, dice_roll):
    assert(dice_roll >=1 and dice_roll <=6) # check precondition 
    assert(body[dict_dice2body[dice_roll]] == 0) # check precondition 

    # ADD CODE HERE 
    return body 

''' 3. TO DO 
    check_full_body()
        Purpose: checks if a body dictionary has all parts
        Input: a body dictionary
        Returns: True if body dictionary contains all keys with value = 1, False otherwise
        Processing: 1. check the value of each key in body dictionary
                    2. If any key is 0 return False
                    3. Otherwise return True 
    No preconditions
'''
def check_full_body(body):
    # ADD CODE and delete pass when done 
    pass

''' 4. TO DO  
    roll_dice 
    Purpose: rolls the dice for a player 
    Input:  the player's name
    Return: the rolled dice value
    Processing:
        1. print message (player_name,"'s turn")
        2. Ask user to press enter to continue (use input)
        3. Wait 0.5 seconds: time.sleep(0.5)
        4. Roll a dice: use random.randint(1,6)
        5. Print message: player_name, "rolled" followed by the dice value
        5. return the dice value
    Preconditions: None
    Postconditions: a dice was rolled
'''
def roll_dice(player_name):
    # ADD CODE HERE
    pass
    

''' 5. TO DO 
    pick_first_player(players)
    Purpose: decides who should roll first. This function is called at the 
            beginning of each game to determine which player should start rolling first 

        Input: players = a list with 2 players names
        Return: the index of the player that will roll first in each round
        Processing: 
            1. Roll a dice for the first player (call roll_dice(players[0]))
            2. Roll a dice for second player   (call roll_dice(players[1]))
            3. While both dice rolls are equal
                print message:  You need to roll again 
                roll again for both players

            4. When dice rolls are not the same, 
                print decision of which player name will go first (the one with the larger roll)
            5. Return the index of the player with the larger roll (0 or 1)

        Preconditions: players is a list with two strings one with the player's name and one with 'Computer'
'''
def pick_first_player(players):
    # ADD YOUR CODE HERE
    pass
    return 0 # replace return 0 with return of the index of the first player to roll 

'''6. TO DO 
    game() 
    Purpose: plays the game once
    Input: player's name
    Return: the name of the winning player
    Processing:
        1. Determine which player starts to roll first in each round
        2. Keep playing rounds until one of the players player fills its beetle
        3. Whenever a new body part is added to either player's beetle, draw the beetle 
        4. return the name of the winning player
    Precondition: None
'''
def game(player_name):
    # initialize your variables
    
    player_names = [player_name, 'Computer'] # a list that stores the names of the players

    index_first = pick_first_player(player_names) #  call function pick_first_player - it will return the index of the first player to roll
    players_turn = [index_first,(index_first +1) % 2] # players_turn = player names in turn order

    players = {player_names[i]:get_empty_body() for i in players_turn} # stores the players' names (as keys) and their 
    # bodies (as values)

    # Add code to play the game. 
    game_over = False # set to True when a player has finished - it will stop the while loop
    winner_name = ""
    while not game_over:

        #ADD CODE HERE 
        # add code to play a round of the game (each player rolls and a part is added or not to their beetle bodies) 
          for player_name, player_body in players.items(): # for each player
             '''
            1. Roll the dice - call roll_dice(player_name)
            2. Call check_add_part()
                the function needs to print a message which part can be added or if not, why. 
            3. If a new part can be added, add the part (call add_part()), and draw the beetle (call draw_beetle)
            4. If the beetle's player is full (call check_full_body()), 
                - print a Win message with the player_name, 
                - set winner_name to player_name
                - set game_over to True 
                - break from for loop
            '''
    
    return winner_name

''' DONE
    get_empty_body()
        Purpose: returns an empty body dictionary
        No inputs
        Returns an empty body dictionary - all parts with a value of 0
        Precondition: None
'''
def get_empty_body():
    return {'body':0, 'head':0, 'leg':0, 'eye':0, 'antenna':0, 'tail':0}

''' DONE
   play_multiple_games() 
   Purpose: plays the game repeatedly: calls the function game() in a loop, when the user enters q it quits. 
   Inputs: None
   Return: None
   Precondition: None
'''
def play_multiple_games():
    answer = input('Press S to start the game or Q to quit: ')
    player_name     = input('Enter your player name: ') # initialize player name

    num_wins   = 0
    num_losses = 0

    while answer.lower() != 'q':
        print('Let''s play')
        winner = game(player_name)
        if winner != 'Computer':
            num_wins += 1
        else:
            num_losses += 1
        answer = input('Press S to start the game or Q to quit: ')

    print('You played', num_wins+num_losses, 'games!')
    print('You won', num_wins, '. Great job!')    
    print('Thank you for playing')


''' DONE
    draw_beetle()            
    Purpose: draws the body of the beetle depending on the existing parts 
    Input: body
        prints the body with the existing parts or a message
    Return: None
    Precondition: all existing body parts follow the rules (e.g. no eyes without a head)
'''
def draw_beetle(body):
    # draws the body of the beetle
    antenna             = '     | |\n'
    top_bottom_head     = '     ---\n'
    middle_head         = '    |   |\n'
    eyes                = '    |. .|\n'
    top_bottom_body     = '   -------\n'
    middle_body         = '  |       |\n'
    legs                = '--|       |--\n'
    tail                = '      |\n'

    count_bodies = sum(body.values())
    
    if count_bodies == 0:
        print('You have no parts so far')
    
    if body['head'] == 1:
        if body['antenna'] == 1: # assumes there is a head
            print(antenna, end='')
        
        if body['eye'] == 1: # print a head with eyes
            print(top_bottom_head + eyes + middle_head + top_bottom_head, end = '')
        else: # print just the head
            print(top_bottom_head + middle_head*2 + top_bottom_head, end = '')
    
    if body['body'] == 1:
        if body['leg'] == 1:
            print(top_bottom_body + legs*3 + top_bottom_body, end = '')
        else:
            print(top_bottom_body + middle_body*3 + top_bottom_body, end = '')

        if body['tail'] == 1:
            print(tail)    

'''
    Add code to test each function below. 
    You need to choose your test cases very carefully. They should test the function works
    correctly through all paths through a function (ifs, else, elis, loops) and for a 
    sufficient values of input parameters. 
    For example for the check_add_body() function add cases that:  
        - Test adding body parts in correct and some in incorrect order
        - Test adding an already existing body part. 
'''
if __name__ == '__main__':
    random.seed()  # initialize the seed to current time. 

    # 1. ADD CODE TO TEST check_add_part(body, dice_roll)
    print("1. TEST check_add_part(body, dice_roll)")
    
    # each test case should be described as follows:
    # replace x with a number from 1 to number of tests you added  
    print("\t Test 1.x add text - describe what case are you testing - be specific")
    print("\t Inputs add text - describe inputs")
    print("\t Expected return add text - describe expected output")
    # add test case
    print("\t Actual return", "add actual return")
    print("\t Test 1.x passed or not")

    # 2. ADD CODE TO TEST add_part(body, dice_roll)
    print("2. TEST add_part(body, dice_roll)")

    # each test case should be described as follows:
    # replace x with a number from 1 to number of tests you added   
    print("\t Test 2.x add text - describe what case are you testing - be specific")
    print("\t Inputs add text - describe inputs")
    print("\t Expected return add text - describe expected output")
    # add test case
    print("\t Actual return", "add actual return")
    print("\t Test 2.x passed or not")

    # 3. ADD CODE TO TEST check_full_body(body)
    print("3. TEST check_full_body(body)")

     # each test case should be described as follows:
    # replace x with a number from 1 to number of tests you added   
    print("\t Test 3.x add text - describe what case are you testing - be specific")
    print("\t Inputs add text - describe inputs")
    print("\t Expected return add text - describe expected output")
    # add test case
    print("\t Actual return", "add actual return")
    print("\t Test 3.x passed or not")

    # 4. ADD CODE TO TEST roll_dice(player_name)
    print("4. TEST roll_dice(player_name)")
     # each test case should be described as follows:
    # replace x with a number from 1 to number of tests you added   
    print("\t Test 4.x add text - describe what case are you testing - be specific")
    print("\t Inputs add text - describe inputs")
    print("\t Expected return add text - describe expected output")
    # add test case
    print("\t Actual return", "add actual return")
    print("\t Test 4.x passed or not")

    # 5. ADD CODE TO TEST pick_first_player(players)
    print("5. TEST pick_first_player(players)")
     # each test case should be described as follows:
    # replace x with a number from 1 to number of tests you added   
    print("\t Test 5.x add text - describe what case are you testing - be specific")
    print("\t Inputs add text - describe inputs")
    print("\t Expected return add text - describe expected output")
    # add test case
    print("\t Actual return", "add actual return")
    print("\t Test 5.x passed or not")

    # 6. ADD CODE TO TEST game(player_name)
    print("6. TEST game(player_name)")
     # each test case should be described as follows:
    # replace x with a number from 1 to number of tests you added   
    print("\t Test 6.x add text - describe what case are you testing - be specific")
    print("\t Inputs add text - describe inputs")
    print("\t Expected return add text - describe expected output")
    # add test case
    print("\t Actual return", "add actual return")
    print("\t Test 6.x passed or not")

    # 7. ADD CODE TO TEST draw_beetle(body)
    print("7. TEST draw_beetle(body)")
     # each test case should be described as follows:
    # replace x with a number from 1 to number of tests you added   
    print("\t Test 7.x add text - describe what case are you testing - be specific")
    print("\t Inputs add text - describe inputs")
    print("\t Expected return add text - describe expected output")
    # add test case
    print("\t Actual return", "add actual return")
    print("\t Test 7.x passed or not")
    

