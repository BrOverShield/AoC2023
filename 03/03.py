import time

#File names
INPUT_FILE_NAME = "input.txt"
TEST_INPUT_1_FILE_NAME = "test1.txt"

#Positions
NUMBER_IS_LEFT = "left"
NUMBER_IS_RIGHT = "right"
EMPTY_STRING = ""

#Magic numbers
NONE = 0
DECREMENT_OF_ONE = -1
MAX_NUMBER_OF_PART_NUMBERS = 2
FIRST = 0
SECOND = 1

#Magic Strings
DOT_CHARACTER = "."
STAR_CHARACTER = "*"
NEW_LINE_CHARACTER = "\n"
FIRST_ROW = 0
FIRST_COLUMN = 0

def IsSymbol(Character):
    if Character.isdigit() or Character == DOT_CHARACTER or Character == NEW_LINE_CHARACTER:
        return False
    else:
        return True
        
def ExtractNumberFromMap(Line, x, Direction = EMPTY_STRING):
    if Direction == NUMBER_IS_RIGHT:
        StartPosition = x
    else:
        StartPosition = NONE
        for Position in range(x,FIRST_COLUMN - 1,DECREMENT_OF_ONE): # -1 because the last iteration is omitted
            StartNumber = Line[Position]
            if not StartNumber.isdigit():
                StartPosition = Position + 1
                break
            elif Position == FIRST_COLUMN:
                StartPosition = FIRST_COLUMN
                break
    
    if Direction == NUMBER_IS_LEFT:
        EndPosition = x
    else:
        EndPosition = NONE
        LastIndex = len(Line) - 2 # Additionnal -1 because of the new line
        for Position in range(x,LastIndex + 1): # +1 because the last iteration is omitted
            EndNumber = Line[Position]
            if not EndNumber.isdigit():
                EndPosition = Position - 1
                break
            elif Position == LastIndex:
                EndPosition = LastIndex
                break
    Number = Line[StartPosition:EndPosition+1] # +1 because the slicing does not include the end bound.
    return int(Number)

'''
Calculates the answer for part 1 of day 03 of Advent of Code 2023
'''
def Part1(Input):
    with open(Input) as file:
        Lines = file.readlines()
        Sum = NONE
        for y, Line in enumerate(Lines):
            for x, Character in enumerate(Line):
                if IsSymbol(Character):
                    #TOP ROW
                    if y != FIRST_ROW:
                        if Lines[y - 1][x].isdigit():
                            Sum = Sum + ExtractNumberFromMap(Lines[y - 1], x)
                        else:
                            if x != FIRST_COLUMN:
                                if Lines[y - 1][x - 1].isdigit(): #Check Top Left
                                    Sum = Sum + ExtractNumberFromMap(Lines[y - 1], x - 1, NUMBER_IS_LEFT)
                            if x != len(Line) - 2: # Additionnal -1 because of the new line
                                if Lines[y - 1][x + 1].isdigit(): #Check Top Right
                                    Sum = Sum + ExtractNumberFromMap(Lines[y - 1], x + 1, NUMBER_IS_RIGHT)
                    #BOTTOM ROW
                    if y != len(Line) - 1:
                        if Lines[y + 1][x].isdigit():
                            Sum = Sum + ExtractNumberFromMap(Lines[y + 1], x)
                        else:
                            if x != FIRST_COLUMN:
                                if Lines[y + 1][x - 1].isdigit(): #Check Bottom Left
                                    Sum = Sum + ExtractNumberFromMap(Lines[y + 1], x - 1, NUMBER_IS_LEFT)
                            if x != len(Line) - 2: # Additionnal -1 because of the new line
                                if Lines[y + 1][x + 1].isdigit(): #Check Bottom Right
                                    Sum = Sum + ExtractNumberFromMap(Lines[y + 1], x + 1, NUMBER_IS_RIGHT)
                    #SIDES
                    if x != FIRST_COLUMN:
                        if Lines[y][x - 1].isdigit():
                            Sum = Sum + ExtractNumberFromMap(Lines[y], x - 1, NUMBER_IS_LEFT)
                    if x != len(Line) - 2: # Additionnal -1 because of the new line
                        if Lines[y][x + 1].isdigit():
                            Sum = Sum + ExtractNumberFromMap(Lines[y], x + 1, NUMBER_IS_RIGHT)
        print(Sum)
'''
Calculates the answer for part 2 of day 03 of Advent of Code 2023
'''
def Part2(Input):
    with open(Input) as file:
        Lines = file.readlines()
        PartNumbers = set()
        Sum = NONE
        for y, Line in enumerate(Lines):
            for x, Character in enumerate(Line):
                if Character == STAR_CHARACTER:
                    PartNumbers = []
                    # TOP ROW
                    if y != FIRST_ROW:
                        if Lines[y - 1][x].isdigit():
                            PartNumber = ExtractNumberFromMap(Lines[y - 1], x)
                            PartNumbers.append(PartNumber)
                        else:
                            if x != FIRST_COLUMN:
                                if Lines[y - 1][x - 1].isdigit():
                                    PartNumber = ExtractNumberFromMap(Lines[y - 1], x - 1, NUMBER_IS_LEFT)
                                    PartNumbers.append(PartNumber)
                            if x != len(Line) - 2: # Additionnal -1 because of the new line
                                if Lines[y - 1][x + 1].isdigit():
                                    PartNumber = ExtractNumberFromMap(Lines[y - 1], x + 1, NUMBER_IS_RIGHT)
                                    PartNumbers.append(PartNumber)
                    # BOTTOM ROW
                    if y != len(Line) - 1:
                        if Lines[y + 1][x].isdigit():
                            if len(PartNumbers) == MAX_NUMBER_OF_PART_NUMBERS:
                                break
                            PartNumber = ExtractNumberFromMap(Lines[y + 1], x)
                            PartNumbers.append(PartNumber)
                        else:
                            if x != FIRST_COLUMN:
                                if Lines[y + 1][x - 1].isdigit():
                                    if len(PartNumbers) == MAX_NUMBER_OF_PART_NUMBERS:
                                        break
                                    PartNumber = ExtractNumberFromMap(Lines[y + 1], x - 1, NUMBER_IS_LEFT)
                                    PartNumbers.append(PartNumber)
                            if x != len(Line) - 2: # Additionnal -1 because of the new line
                                if Lines[y + 1][x + 1].isdigit():
                                    if len(PartNumbers) == MAX_NUMBER_OF_PART_NUMBERS:
                                        break
                                    PartNumber = ExtractNumberFromMap(Lines[y + 1], x + 1, NUMBER_IS_RIGHT)
                                    PartNumbers.append(PartNumber)

                    # ON THE SIDES
                    if x != FIRST_COLUMN:
                        if Lines[y][x - 1].isdigit():
                            if len(PartNumbers) == MAX_NUMBER_OF_PART_NUMBERS:
                                break
                            PartNumber = ExtractNumberFromMap(Lines[y], x - 1, NUMBER_IS_LEFT)
                            PartNumbers.append(PartNumber)
                    if x != len(Line) - 2: # Additionnal -1 because of the new line
                        if Lines[y][x + 1].isdigit():
                            if len(PartNumbers) == MAX_NUMBER_OF_PART_NUMBERS:
                                break
                            PartNumber = ExtractNumberFromMap(Lines[y], x + 1, NUMBER_IS_RIGHT)
                            PartNumbers.append(PartNumber)

                    if len(PartNumbers) == MAX_NUMBER_OF_PART_NUMBERS:
                        Sum = Sum + (PartNumbers[FIRST] * PartNumbers[SECOND])
        print(Sum)

StartTime = time.time()
#Part1(TEST_INPUT_1_FILE_NAME)
#Part1(INPUT_FILE_NAME)
#Part2(TEST_INPUT_1_FILE_NAME)
#Part2(INPUT_FILE_NAME)
EndTime = time.time()
print("Time: " + str(EndTime - StartTime))