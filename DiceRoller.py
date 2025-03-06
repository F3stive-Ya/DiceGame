# Created and commented by Shane Borges (F3estive-Ya)
# Description: A program that simulates dice rolls, and displays contrained visual data

from Dice_Helper import Function1, Function2, Function3

loop = True
roll_time = 0
def main():
    global loop
    prompt = "Rolling Times (1-10000, 0 to stop.) "
    roll_time = Function1(1,10000,prompt,"Invalid Number")
    if (roll_time != 0):
        loop = True
        Function2(roll_time)
        
        #import variables after assigned value in Function2
        from Dice_Helper import facetuple
        
        face_one, face_two, face_three,\
              face_four, face_five, face_six = facetuple
        Function3("One  :",face_one,"=",face_one)
        Function3("Two  :",face_two,"=",face_two)
        Function3("Three:",face_three,"=",face_three)
        Function3("Four :",face_four,"=",face_four)
        Function3("Five :",face_five,"=",face_five)
        Function3("Six  :",face_six,"=",face_six)
    else:
        print("Thank you")
        loop = False

while loop:
    main()
