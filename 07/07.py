import time

# File names
INPUT_FILE_NAME = "input.txt"
TEST_INPUT_1_FILE_NAME = "test1.txt"

#Magic Strings
ALPHABET = ["A","K","Q","J","T","9","8","7","6","5","4","3","2"]
JOKER_ALPHABET = ["A","K","Q","T","9","8","7","6","5","4","3","2","J"]
JOKER = "J"

SPACE_SEPERATOR = " "

#Magic Numbers
NONE = 0
CARDS_PER_HAND = 5
VALUE = 1
BID = 1

FIRST_ITEM = 0
SECOND_ITEM = 1

FOUR_OF_A_KIND = 4
THREE_OF_A_KIND = 3
PAIR = 2

'''
Calculates the amount of each card there is in a hand and sorts them from most card to least.
'''
def GetQuantities(Line):
    Line = res = ''.join(sorted(Line))
    Total = NONE
    Amounts = {}
    while Total != CARDS_PER_HAND:
        Char = Line[Total]
        Count = Line.count(Char)
        Total = Total + Count
        Amounts[Char] = Count
    Amounts = dict(sorted(Amounts.items(), key=lambda item: item[VALUE], reverse=True))
    return Amounts

'''
Sorts a list of hands based off of their strength using the card alphabet
'''
def SortDictionaryByKey(Type):
    Keys = list(Type.keys())
    Keys.sort(key=GetStrength)
    return {i: Type[i] for i in Keys}

'''
Sorts a list of hands based off of their strength using the joker alphabet
'''
def JokerSortDictionaryByKey(Type):
    Keys = list(Type.keys())
    Keys.sort(key=GetJokerStrength)
    return {i: Type[i] for i in Keys}

'''
Calculates the strength of a hand based off the card alphabet
'''
def GetStrength(word):
    return [ALPHABET.index(c) for c in word]

'''
Calculates the strength of a hand based off the joker alphabet
'''
def GetJokerStrength(word):
    return [JOKER_ALPHABET.index(c) for c in word]

'''
Calculates the answer for part 1 of day 07 of Advent of Code 2023
'''
def Part1(Input):
    with open(Input) as file:
        Lines = file.readlines()

        Fives = {}
        Fours = {}
        FullHouses = {}
        Threes = {}
        TwoPairs = {}
        Pairs = {}
        HighCards = {}

        for Line in Lines:
            Hand = Line[:CARDS_PER_HAND]
            Amounts = GetQuantities(Hand)
            Bid = int(Line.split(SPACE_SEPERATOR)[BID])

            if list(Amounts.values())[FIRST_ITEM] == CARDS_PER_HAND:
                Fives[Hand] = Bid
            elif list(Amounts.values())[FIRST_ITEM] == FOUR_OF_A_KIND:
                Fours[Hand] = Bid
            elif list(Amounts.values())[FIRST_ITEM] == THREE_OF_A_KIND:
                if list(Amounts.values())[SECOND_ITEM] == PAIR:
                    FullHouses[Hand] = Bid
                else:
                    Threes[Hand] = Bid
            elif list(Amounts.values())[FIRST_ITEM] == PAIR:
                if list(Amounts.values())[SECOND_ITEM] == PAIR:
                    TwoPairs[Hand] = Bid
                else:
                    Pairs[Hand] = Bid
            else:
                HighCards[Hand] = Bid

        Fives = SortDictionaryByKey(Fives)
        Fours = SortDictionaryByKey(Fours)
        FullHouses = SortDictionaryByKey(FullHouses)
        Threes = SortDictionaryByKey(Threes)
        TwoPairs = SortDictionaryByKey(TwoPairs)
        Pairs = SortDictionaryByKey(Pairs)
        HighCards = SortDictionaryByKey(HighCards)

        Types = [Fives, Fours, FullHouses, Threes, TwoPairs, Pairs, HighCards]

        Rank = len(Lines)
        Answer = NONE

        for Type in Types:
            for Bid in list(Type.values()):
                Answer = Answer + (Bid * Rank)
                Rank = Rank - 1

        print(Answer)

'''                 
Calculates the answer for part 2 of day 07 of Advent of Code 2023
'''
def Part2(Input):
    with open(Input) as file:
        Lines = file.readlines()

        Fives = {}
        Fours = {}
        FullHouses = {}
        Threes = {}
        TwoPairs = {}
        Pairs = {}
        HighCards = {}

        for Line in Lines:
            Hand = Line[:CARDS_PER_HAND]
            Amounts = GetQuantities(Hand)
            if JOKER in Amounts:
                if JOKER == list(Amounts.keys())[FIRST_ITEM]:
                    if len(Amounts) > 1:
                        SecondHighest = list(Amounts.keys())[SECOND_ITEM]
                        Amounts[SecondHighest] = Amounts[SecondHighest] + Amounts[JOKER]
                        Amounts.pop(JOKER)
                else:
                    Highest = list(Amounts.keys())[FIRST_ITEM]
                    Amounts[Highest] = Amounts[Highest] + Amounts[JOKER]
                    Amounts.pop(JOKER)

            Bid = int(Line.split(SPACE_SEPERATOR)[BID])

            if list(Amounts.values())[FIRST_ITEM] == CARDS_PER_HAND:
                Fives[Hand] = Bid
            elif list(Amounts.values())[FIRST_ITEM] == FOUR_OF_A_KIND:
                Fours[Hand] = Bid
            elif list(Amounts.values())[FIRST_ITEM] == THREE_OF_A_KIND:
                if list(Amounts.values())[SECOND_ITEM] == PAIR:
                    FullHouses[Hand] = Bid
                else:
                    Threes[Hand] = Bid
            elif list(Amounts.values())[FIRST_ITEM] == PAIR:
                if list(Amounts.values())[SECOND_ITEM] == PAIR:
                    TwoPairs[Hand] = Bid
                else:
                    Pairs[Hand] = Bid
            else:
                HighCards[Hand] = Bid

        Fives = JokerSortDictionaryByKey(Fives)
        Fours = JokerSortDictionaryByKey(Fours)
        FullHouses = JokerSortDictionaryByKey(FullHouses)
        Threes = JokerSortDictionaryByKey(Threes)
        TwoPairs = JokerSortDictionaryByKey(TwoPairs)
        Pairs = JokerSortDictionaryByKey(Pairs)
        HighCards = JokerSortDictionaryByKey(HighCards)

        Types = [Fives, Fours, FullHouses, Threes, TwoPairs, Pairs, HighCards]

        Rank = len(Lines)
        Answer = NONE

        for Type in Types:
            for Bid in list(Type.values()):
                Answer = Answer + (Bid * Rank)
                Rank = Rank - 1

        print(Answer)

StartTime = time.time()
#Part1(TEST_INPUT_1_FILE_NAME)
#Part1(INPUT_FILE_NAME)
#Part2(TEST_INPUT_1_FILE_NAME)
#Part2(INPUT_FILE_NAME)
EndTime = time.time()
print("Time: " + str(EndTime - StartTime))