import time

#File names
INPUT_FILE_NAME = "input.txt"
TEST_INPUT_1_FILE_NAME = "test1.txt"

#Magic numbers
NONE = 0

GAME_ID_PORTION = 0
ROUNDS_PORTION = 1

NUMBER_PORTION = 0
COLOUR_PORTION = 1

SKIP_START = 5

RED_MAX_NUMBER = 12
GREEN_MAX_NUMBER = 13
BLUE_MAX_NUMBER = 14

#Magic strings
RED_COLOUR = "red"
GREEN_COLOUR = "green"
BLUE_COLOUR = "blue"

GAME_ID_DELIMITER = ":"
ROUNDS_DELIMITER = ";"
SETS_DELIMITER = ","
SPACE_CHARACTER = " "

'''
Calculates the answer for part 1 of day 02 of Advent of Code 2023
'''
def Part1(Input):
    with open(Input) as file:
        Lines = file.readlines()
        Sum = NONE
        for Line in Lines:
            ID = int(Line[SKIP_START:].split(GAME_ID_DELIMITER)[GAME_ID_PORTION])
            Rounds = Line[SKIP_START:].split(GAME_ID_DELIMITER)[ROUNDS_PORTION].split(ROUNDS_DELIMITER)
            Info = {RED_COLOUR:NONE, GREEN_COLOUR:NONE, BLUE_COLOUR:NONE}
            for Round in Rounds:
                Sets = Round.split(SETS_DELIMITER)
                for Set in Sets:
                    Stripped = Set.strip()
                    Split = Stripped.split(SPACE_CHARACTER)
                    Number = int(Split[NUMBER_PORTION])
                    Colour = Split[COLOUR_PORTION]
                    if Info[Colour] < Number:
                        Info[Colour] = Number
            if Info[RED_COLOUR] <= RED_MAX_NUMBER and Info[GREEN_COLOUR] <= GREEN_MAX_NUMBER and Info[BLUE_COLOUR] <= BLUE_MAX_NUMBER:
                Sum = Sum + ID
        print(Sum)
'''
Calculates the answer for part 2 of day 02 of Advent of Code 2023
'''
def Part2(Input):
    with open(Input) as file:
        Lines = file.readlines()
        Sum = NONE
        for Line in Lines:
            Rounds = Line[SKIP_START:].split(":")[ROUNDS_PORTION].split(";")
            Info = {RED_COLOUR:NONE, GREEN_COLOUR:NONE, BLUE_COLOUR:NONE}
            for Round in Rounds:
                Sets = Round.split(",")
                for Set in Sets:
                    Stripped = Set.strip()
                    Split = Stripped.split(" ")
                    Number = int(Split[NUMBER_PORTION])
                    Colour = Split[COLOUR_PORTION]
                    if Info[Colour] < Number:
                        Info[Colour] = Number
            Sum = Sum + (Info[RED_COLOUR] * Info[GREEN_COLOUR] * Info[BLUE_COLOUR])
        print(Sum)

StartTime = time.time()
#Part1(TEST_INPUT_1_FILE_NAME)
#Part1(INPUT_FILE_NAME)
#Part2(TEST_INPUT_1_FILE_NAME)
#Part2(INPUT_FILE_NAME)
EndTime = time.time()
print("Time: " + str(EndTime - StartTime))