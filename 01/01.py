#File names
INPUT_FILE_NAME = "input.txt"
TEST_INPUT_1_FILE_NAME = "test.txt"
TEST_INPUT_2_FILE_NAME = "test2.txt"

#Constants to make it easier to read and understand
NUMBER_NOT_FOUND = "ERROR"

#Magic numbers
NONE = 0
FIRST_LETTER = 0
FIRST_NUMBER = 0


#Magic strings
CHARACTER_NUMBER_ONE = "1"
CHARACTER_NUMBER_TWO = "2"
CHARACTER_NUMBER_THREE = "3"
CHARACTER_NUMBER_FOUR = "4"
CHARACTER_NUMBER_FIVE = "5"
CHARACTER_NUMBER_SIX = "6"
CHARACTER_NUMBER_SEVEN = "7"
CHARACTER_NUMBER_EIGHT = "8"
CHARACTER_NUMBER_NINE = "9"

SPELT_NUMBER_ONE = "one"
SPELT_NUMBER_TWO = "two"
SPELT_NUMBER_THREE = "three"
SPELT_NUMBER_FOUR = "four"
SPELT_NUMBER_FIVE = "five"
SPELT_NUMBER_SIX = "six"
SPELT_NUMBER_SEVEN = "seven"
SPELT_NUMBER_EIGHT = "eight"
SPELT_NUMBER_NINE = "nine"

#Converters
NUMBERS_MAP = {
    SPELT_NUMBER_ONE:CHARACTER_NUMBER_ONE,
    SPELT_NUMBER_TWO:CHARACTER_NUMBER_TWO,
    SPELT_NUMBER_THREE:CHARACTER_NUMBER_THREE,
    SPELT_NUMBER_FOUR:CHARACTER_NUMBER_FOUR,
    SPELT_NUMBER_FIVE:CHARACTER_NUMBER_FIVE,
    SPELT_NUMBER_SIX:CHARACTER_NUMBER_SIX,
    SPELT_NUMBER_SEVEN:CHARACTER_NUMBER_SEVEN,
    SPELT_NUMBER_EIGHT:CHARACTER_NUMBER_EIGHT,
    SPELT_NUMBER_NINE:CHARACTER_NUMBER_NINE}
    
SPELT_NUMBERS = list(NUMBERS_MAP.keys())

'''
Returns the first number it encounters in a given string.
'''
def FindFirstNumber (Line):
    for Character in Line:
        if Character.isdigit():
            return Character
    print("No number found in: " & Line)
    quit()

'''
Returns all numbers, numeric or spelt out, found in a string in the order that they were found.
'''                 
def ExtractSpeltAndNumericNumbers(Line):
    NumbersFound = ""
    for Index, Character in enumerate(Line):
        if Character.isdigit():
            NumbersFound = NumbersFound + Character
        else:
            for SpeltNumber in SPELT_NUMBERS:
                if Character == SpeltNumber[FIRST_LETTER]:
                    if len(Line[Index:]) >= len(SpeltNumber):
                        EndBound = Index + len(SpeltNumber)
                        if Line[Index:EndBound] == SpeltNumber:
                            NumbersFound = NumbersFound + NUMBERS_MAP[SpeltNumber]
    return NumbersFound

'''
Calculates the answer for part 1 of day 01 of Advent of Code 2023
'''
def Part1(Input):
    with open(Input) as file:
        Lines = file.readlines()
        Sum = NONE
        for Line in Lines:
            FirstNumber = FindFirstNumber(Line)
            ReversedLine = Line[::-1]
            LastNumber = FindFirstNumber(ReversedLine)
            NewNumber = str(FirstNumber) + str(LastNumber)
            Sum = Sum + int(NewNumber) 
        print(Sum)

'''
Calculates the answer for part 2 of day 01 of Advent of Code 2023
'''
def Part2(Input):
    with open(Input) as file:
        Lines = file.readlines()
        Sum = NONE
        for Line in Lines:
            ExtractedNumbers = ExtractSpeltAndNumericNumbers(Line)
            FirstNumber = ExtractedNumbers[FIRST_NUMBER]
            ReversedLine = ExtractedNumbers[::-1]
            LastNumber = ReversedLine[FIRST_NUMBER]
            NewNumber = str(FirstNumber) + str(LastNumber)
            Sum = Sum + int(NewNumber)
        print(Sum)

#Part1(TEST_INPUT_1_FILE_NAME)
#Part1(INPUT_FILE_NAME)
#Part2(TEST_INPUT_2_FILE_NAME)
#Part2(INPUT_FILE_NAME)