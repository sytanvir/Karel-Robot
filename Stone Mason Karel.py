from karel.stanfordkarel import *

"""
File: main.py
--------------------
When you finish writing this file, Karel should have repaired 
each of the columns in the temple
"""

def main():
   #First_cokumn
   turn_left()
   build_a_column()
   
   #secound column
   turn_right()
   move_four_step()
   turn_right()
   build_a_column()
   
   #Third_column
   turn_left()
   move_four_step()
   turn_left()
   build_a_column()
   
   #Fourth_column
   turn_right()
   move_four_step()
   turn_right()
   build_a_column()
   
   turn_left()
   
   
#my functions   
# make four moves  
def move_four_step():
    move()
    move()
    move()
    move()
    
# Build One column
def build_a_column():
    put_beeper()
    #For loop
    for x in range(4):
       walk_put()
       
#karel make step and put beeper
def walk_put():
    move()
    put_beeper()
    
def turn_right():
    turn_left()
    turn_left()
    turn_left()

if __name__ == '__main__':
    main()