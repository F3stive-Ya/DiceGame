# Created and Commented by Shane Borges (F3stive-Ya)
# Description: This file has three functions, the first prompts the user, \
# the second rolls the dice, and the third displays the data. It is a helper file for the main file.

import random


def Function1( low_x, high_x, prompt, error ):
    var = int(input( prompt ))
    global face_one, face_two, face_three, face_four, face_five, face_six
    
    #Check to see if variable is valid
    if ( var >= low_x and high_x >= var ):
        face_one = 0
        face_two = 0
        face_three = 0
        face_four = 0
        face_five = 0
        face_six = 0
    elif ( var < 0 or var > high_x):
        while ( var < 0 or var > high_x):
            print(error)
            var = int(input(prompt))
            if ( var == 0 ):
                return var
    else:
        return var
    return var
    
def Function2( roll_times ):
    global face_one, face_two, face_three, face_four, face_five, face_six, facetuple

    #"Randomly" picks a number from 1-6 as many times as entered
    for x in range( 0, roll_times ):
        x += 1
        var = random.randint(1, 6)
        if ( var == 1 ):
            face_one += 1
        elif ( var == 2 ):
            face_two += 1
        elif ( var == 3 ):
            face_three += 1
        elif ( var == 4 ):
            face_four += 1
        elif ( var == 5 ):
            face_five += 1
        elif ( var == 6  ):
            face_six += 1
    facetuple = face_one, face_two, face_three, face_four, face_five, face_six
    
    
def Function3( title, length, chtr, note ):

    #Find the die face with the most rolls
    best_Side = max( facetuple )
    
    #Divides the inputted face by the face with the most rolls, then multiplies
    max_results = round(( length / best_Side ) * 70)
    length = int( max_results )

    print(f'{title}{length * chtr} {note}')
    
    
    



