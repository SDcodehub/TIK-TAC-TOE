from IPython.display import clear_output
clear_output()
#game_list = [1,2,3]
#game_list2 = [4,5,6]
#game_list3 = [7,8,9]
def display_game(game_list):
    print("WELCOME TO TIK TAC TOE")
    print("Current board position")
    print (str(game_list [0]) + "   |   "+ str(game_list [1]) + "   |   "+str(game_list [2]))
    print ("-----------------")
    print (str(game_list [3]) + "   |   "+ str(game_list [4]) + "   |   "+str(game_list [5]))
    print ("-----------------")
    print (str(game_list [6]) + "   |   "+ str(game_list [7]) + "   |   "+str(game_list [8]))
    print ("-----------------")
#display_game(game_list1,game_list2,game_list3)
def position_choice():
    
    # This original choice value can be anything that isn't an integer
    choice = 'wrong'
    
    
    # While the choice is not a digit, keep asking for input.
    while choice not in validchoice:
        
        
        # we shouldn't convert here, otherwise we get an error on a wrong input
        choice = input("Pick a position to replace {}: ".format (validchoice))
        
        if choice not in validchoice:
            # THIS CLEARS THE CURRENT OUTPUT BELOW THE CELL
            #clear_output()
            
            print("Sorry, but you did not choose a valid position {}".format (validchoice))
        else:
            validchoice.remove(choice)
    
    # Optionally you can clear everything after running the function
    # clear_output()
    
    # We can convert once the while loop above has confirmed we have a digit.
            return int(choice)

def replacement_choice(game_list,position,playerone,playertwo):
    
    #user_placement = input("Type a string to place at the position")
    if count%2==0 or count==0:
    
        user_placement = playerone
    else:
        user_placement = playertwo
    
    position = position -1
    
    game_list[position] = user_placement
        
    return game_list

def gameon_choice():
  
  # This original choice value can be anything that isn't a Y or N
  choice = 'wrong'
  

  # While the choice is not a digit, keep asking for input.
  while choice not in ['y','n']:
      
      # we shouldn't convert here, otherwise we get an error on a wrong input
      choice = input("Game over! Would you like to play again? Y or N ")

      #MAKE SURE USER INPUT IS CONSISTENT, Y become y
      choice = choice.lower()
      if choice not in ['y','n']:
          # THIS CLEARS THE CURRENT OUTPUT BELOW THE CELL
          clear_output()
          
          print("Sorry, I didn't understand. Please make sure to choose Y or N.")
          
  
  # Optionally you can clear everything after running the function
  # clear_output()
  
  if choice == "y":
      # Game is still on
      return True
  else:
      # Game is over
      return False

def gameon_choice2(checksym, playername):
    
    indices = [i for i, x in enumerate(game_list) if x == checksym]
    check= [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]

    c = []

    for each in check:
        
        if len(c) != 3:
    
            c = [item for item in each if item in indices]
            #print (c)
            if len(c) == 3:
                print("Game own! by " + playername + " ({})".format(checksym))
               
                return False
            else:
            #Game is not over
                status =  True
    return(status)

def PlayerSym_choice():
    # This original choice value can be anything that isn't a Y or N
    choice = 'wrong'
    
    # While the choice is not a digit, keep asking for input.
    while choice not in ['x','o']:
        
        choice = input("Choose symbol for Player1: x or o ")
            
        if choice not in ['x','o']:
            
            # THIS CLEARS THE CURRENT OUTPUT BELOW THE CELL
            clear_output()
            
            print("Sorry, but you did not choose a valid symbol x or o ")
            
    return(choice)
     #Plyer2choice    
    
def playertwochoice ():
    if playerone == "x":
        playertwo="o"
    else:
        playertwo="x"
    return(playertwo)

# Variable to keep game playing
game_on_first = True
game_on_second = True
# First Game List
game_list = [" "," "," "," "," "," "," "," "," "]

count = 0

playerone = PlayerSym_choice()
print("player One")
print(playerone)
playertwo = playertwochoice ()

#valid choice update as game progresses
validchoice = ["1","2","3","4","5","6","7","8","9"]
display_game(game_list)

while count <= 8 and game_on_first and game_on_second:
    
    # Clear any historical output and show the game list
    clear_output()
    # Have player choose position
    position = position_choice()
    position
    
    # Rewrite that position and update game_list
    game_list = replacement_choice(game_list,position,playerone,playertwo)

    count = count + 1
    
    # Clear Screen and show the updated game list
    #clear_output()
    display_game(game_list)

    # Ask if you want to keep playing
    game_on_first = gameon_choice2(playerone, "playerone")
    game_on_second = gameon_choice2(playertwo, "playertwo")
    
    if game_on_first is False or game_on_second is False:
      game_on = gameon_choice()
      if game_on:
        clear_output()
        count = 0
        game_on_first = True
        game_on_second = True
        # First Game List
        game_list = [" "," "," "," "," "," "," "," "," "]
        count = 0
        playerone = PlayerSym_choice()
        playertwo = playertwochoice ()

        #valid choice update as game progresses
        validchoice = ["1","2","3","4","5","6","7","8","9"]
    elif count > 8:
      game_on = gameon_choice()
      if game_on:
        clear_output()
        count = 0
        game_on_first = True
        game_on_second = True
        # First Game List
        game_list = [" "," "," "," "," "," "," "," "," "]
        count = 0
        playerone = PlayerSym_choice()
        playertwo = playertwochoice ()

        #valid choice update as game progresses
        validchoice = ["1","2","3","4","5","6","7","8","9"]
