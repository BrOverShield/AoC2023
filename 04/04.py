import time

# File names
INPUT_FILE_NAME = "input.txt"
TEST_INPUT_1_FILE_NAME = "test1.txt"

#Magic Numbers
NONE = 0
FIRST_PART = 0
SECOND_PART = 1
SKIP_START_CHARACTERS = 5
ONE_CARD = 1

#Magic Strings
GAME_ID_DELIMITER = ":"
NUMBERS_DELIMITER = "|"
DOUBLE_SPACE = "  "
SINGLE_SPACE = " "
'''
Calculates the answer for part 1 of day 04 of Advent of Code 2023
'''
def Part1(Input):
    with open(Input) as file:
        Lines = file.readlines()
        Sum = NONE
        for Card in Lines:
            Card = Card.split(GAME_ID_DELIMITER)[SECOND_PART]
            WinningNumbers = Card.split(NUMBERS_DELIMITER)[FIRST_PART]
            WinningNumbers = WinningNumbers.strip()
            WinningNumbers = WinningNumbers.replace(DOUBLE_SPACE, SINGLE_SPACE)
            WinningNumbers = WinningNumbers.split(SINGLE_SPACE)

            YourNumbers = Card.split(NUMBERS_DELIMITER)[SECOND_PART]
            YourNumbers = YourNumbers.strip()
            YourNumbers = YourNumbers.replace(DOUBLE_SPACE, SINGLE_SPACE)
            YourNumbers = YourNumbers.split(SINGLE_SPACE)
            Found = NONE
            for Number in YourNumbers:
                if Number in WinningNumbers:
                    Found = Found + 1
            if Found:
                Sum = Sum + pow(2,Found - 1) # -1 because i number found is 1 point, not 2
        print(Sum)

'''
Calculates the answer for part 2 of day 04 of Advent of Code 2023
'''
def Part2(Input):
    with open(Input) as file:
        Lines = file.readlines()
        Sum = NONE
        QuantityOfCards = {}
        for Card in Lines:
            CardNumber = Card[SKIP_START_CHARACTERS:]
            CardNumber = CardNumber.split(GAME_ID_DELIMITER)[FIRST_PART]
            CardNumber = int(CardNumber)
            Card = Card.split(GAME_ID_DELIMITER)[SECOND_PART]
            WinningNumbers = Card.split(NUMBERS_DELIMITER)[FIRST_PART]
            WinningNumbers = WinningNumbers.strip()
            WinningNumbers = WinningNumbers.replace(DOUBLE_SPACE, SINGLE_SPACE)
            WinningNumbers = WinningNumbers.split(SINGLE_SPACE)

            YourNumbers = Card.split(NUMBERS_DELIMITER)[SECOND_PART]
            YourNumbers = YourNumbers.strip()
            YourNumbers = YourNumbers.replace(DOUBLE_SPACE, SINGLE_SPACE)
            YourNumbers = YourNumbers.split(SINGLE_SPACE)

            if CardNumber in QuantityOfCards:
                Quantity = QuantityOfCards[CardNumber] + 1 # +1 because you count also the original card.
            else:
                Quantity = ONE_CARD

            Sum = Sum + Quantity

            Found = NONE
            for Number in YourNumbers:
                if Number in WinningNumbers:
                    Found = Found + 1
            if Found:
                for NextCardNumber in range(CardNumber + 1,CardNumber + Found + 1): # Must add +1 to the end bound as the end bound is not inclusive.
                    if NextCardNumber in QuantityOfCards:
                        QuantityOfCards[NextCardNumber] = QuantityOfCards[NextCardNumber] + Quantity
                    else:
                        QuantityOfCards[NextCardNumber] = Quantity
        print(Sum)


StartTime = time.time()
#Part1(TEST_INPUT_1_FILE_NAME)
#Part1(INPUT_FILE_NAME)
#Part2(TEST_INPUT_1_FILE_NAME)
#Part2(INPUT_FILE_NAME)
EndTime = time.time()
print("Time: " + str(EndTime - StartTime))