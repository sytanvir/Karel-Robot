from karel.stanfordkarel import *

"""
Karel should fill the whole world with beepers.
"""


def main():
    """
    You should write your code to make Karel do its task in
    this function. Make sure to delete the 'pass' line before
    starting to write your own code. You should also delete this
    comment and replace it with a better, more descriptive one.
    """
    
    # when world has more than one column it will execute this loop
    if front_is_clear():
        while left_is_clear():
            build_a_row()
            come_back()
            go_to_next_row()
        build_a_row()
        move_to_wall()
        
    # To execute Single column world
    else:
        turn_left()
        build_a_row()
        come_back()
        turn_right()
        
     
     
# To make a entire row 
def build_a_row():
    while front_is_clear():
        single_pattern_block()
        
        
        
# makes a basic pattern with two position
# puts a beeper and moves if path is clear
# When karel could move twice it will put a beeper if there is no beeper.
# when karel made one move and get bloacked,karel will stop putting beeper whether beeper exist or not
def single_pattern_block():
    put_beeper()
    if front_is_clear():
        move()
    if front_is_clear():
        move()
        if front_is_blocked():
            if no_beepers_present():
                put_beeper()
                

               
# Karel will come back to first column 
# Pre Condition:First column and Facing east
# post condition: First column and facing east
def come_back():
    turn_around()
    while front_is_clear():
            move()
    turn_around()
    
    
    
# Karel will move to the next row
# here pre and post condition are vice-versa and change at evry step to next row.
def go_to_next_row():
    if left_is_clear():
        if beepers_present():# beeper is  present so post condition: second column facing east
            turn_left()
            move()
            turn_right()
            move() # post condition: Second column
         
        else: # beeper is not present so post condition: First column facing east  
            turn_left()
            move()
            turn_right() 
            
            
            
# Karel will move to the wall when pattern is done.
def move_to_wall():
    come_back()
    turn_right()
    while front_is_clear():
        move()
    turn_left()
    
    
    
# karel will turn right.            
def turn_right():
    for i in range(3):
        turn_left()
        
        

# Karel will turn 180 degree
def turn_around():
    for i in range(2):
        turn_left()

    
    


# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()