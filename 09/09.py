import time
from math import gcd

# File names
INPUT_FILE_NAME = "input.txt"
TEST_INPUT_1_FILE_NAME = "test1.txt"

#Magic Numbers
NONE = 0
FIRST_ITEM = 0
LAST_ITEM = -1

#Magic Strings
FORWARD = "F"
BACKWARD = "B"
NUMBER_SEPERATOR = " "

'''
Gets the next number of the derivatives from the readings in the direction specified
'''
def FindNextNumber(Readings, Direction = FORWARD):
    Derivatives = []
    AllZeros = True
    for Index, Number in enumerate(Readings):
        if Index == len(Readings) - 1: # -1 because starts at 1 instead of 0
            break
        Derivative = Readings[Index + 1] - Readings[Index]
        Derivatives.append(Derivative)
        if AllZeros and Derivative != NONE:
            AllZeros = False

    if AllZeros:
        return Readings[FIRST_ITEM]
    else:
        if Direction == BACKWARD:
            return Readings[FIRST_ITEM] - FindNextNumber(Derivatives, BACKWARD)
        else:
            return Readings[LAST_ITEM] + FindNextNumber(Derivatives)

'''
Calculates the answer for part 1 of day 09 of Advent of Code 2023
'''
def Part1(Input):
    with open(Input) as file:
        Lines = file.readlines()
        Answer = NONE
        for Line in Lines:
            Readings = [int(number) for number in Line.split(NUMBER_SEPERATOR)]
            NextNumber = FindNextNumber(Readings)
            Answer = Answer + NextNumber

        print(Answer)

'''                 
Calculates the answer for part 2 of day 09 of Advent of Code 2023
'''
def Part2(Input):
    with open(Input) as file:
        Lines = file.readlines()
        Answer = NONE
        for Line in Lines:
            Readings = [int(number) for number in Line.split(NUMBER_SEPERATOR)]
            NextNumber = FindNextNumber(Readings, BACKWARD)
            Answer = Answer + NextNumber
        print(Answer)

StartTime = time.time()
#Part1(TEST_INPUT_1_FILE_NAME)
#Part1(INPUT_FILE_NAME)
#Part2(TEST_INPUT_1_FILE_NAME)
#Part2(INPUT_FILE_NAME)
EndTime = time.time()
print("Time: " + str(EndTime - StartTime))