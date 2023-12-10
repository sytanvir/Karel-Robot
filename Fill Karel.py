from karel.stanfordkarel import *

"""
Karel should fill the whole world with beepers.
"""


def main():
#pre condition:first row firts column facing east
#post condition:last row last column facing east 

    while left_is_clear():
        fill_a_row()
        back_to_corner()
        next_row()
    fill_a_row()
    
        
def fill_a_row():
#pre codition:karel facing east 
#post condition:karel facing east
    while front_is_clear():
        step_beeper()
    put_beeper()
    
    
def step_beeper():
    #pre_condition:facing east
    #post-condition:faceing east
    if front_is_clear():
        put_beeper()
        move()
    
        
def back_to_corner():
    #karel back to it's initial corner where it started putting beepers
    turn_around()
    while front_is_clear():
        move()
    turn_around()
    
def next_row():
    #karel move to next row facing east
    turn_left()
    move()
    turn_right()
    
def turn_right():
    #turn left three times in order to turn right 
    for j in range(3):
        turn_left()
        

def turn_around():
    #turn_left twice in order to tunr around
    for i in range(2):
        turn_left()

    


# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()