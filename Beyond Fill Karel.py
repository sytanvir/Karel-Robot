from karel.stanfordkarel import *

"""
Karel should paint the whole world, any color you want. 
As an extension, have karel randomly paint each corner.
"""


def main():
    """
    You should write your code to make Karel do its task in
    this function. Make sure to delete the 'pass' line before
    starting to write your own code. You should also delete this
    comment and replace it with a better, more descriptive one.
    
    """
    while front_is_clear():
        row()
        next_row()
 #complete a whole row with random color and back to precondition(facing east at 1,1 corner)  
def row():
    while front_is_clear():
        fill_corner()
   
    if random():
        paint_corner("blue")
    else: 
        paint_corner("red")
    back()

#fill a single corner with random color           
def fill_corner():
    if random():
        paint_corner("blue")
    else: 
        paint_corner("red")
    move()
#to back to its initail corner 
def back():
    turn_around()
    while front_is_clear():
        move()
    turn_around()
#to move to next row    
def next_row():
    turn_left()
    move()
    turn_right()
    
def turn_right():
    for i in range(3):
        turn_left()
        
def turn_around():
    for i in range(2):
        turn_left()

# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()