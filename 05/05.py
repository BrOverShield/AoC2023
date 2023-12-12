import time

# File names
INPUT_FILE_NAME = "input.txt"
TEST_INPUT_1_FILE_NAME = "test1.txt"

#Magic Strings
SEEDS_DELIMITER = ":"
NUMBER_SEPERATOR = " "

SOURCE_START_NUMBER = "Source Start"
DESTINATION_START_NUMBER = "Destination Start"
LENGTH = "Length"
SOURCE_END_NUMBER = "Source End"
DESTINATION_END_NUMBER = "Destination End"
START_NUMBER = "Start"
END_NUMBER = "End"

#Magic Numbers
FIRST_NUMBER = 0
SECOND_NUMBER = 1
THIRD_NUMBER = 2

FIRST_ITEM = 0
SECOND_ITEM = 1
LAST_ITEM = -1

MOVE_UP_2_LINES = 2
NEXT_EMPTY_LINE = 1
NEXT_NUMBER = 1

HIGHEST_VALUE = 999999999

'''
Parses important information from a line from a conversion table and returns them as a map.
'''
def CreateMap(Line):
    Map = {}
    Map[DESTINATION_START_NUMBER] = int(Line.split(NUMBER_SEPERATOR)[FIRST_NUMBER])
    Map[SOURCE_START_NUMBER] = int(Line.split(NUMBER_SEPERATOR)[SECOND_NUMBER])
    Map[LENGTH] = int(Line.split(NUMBER_SEPERATOR)[THIRD_NUMBER])
    Map[SOURCE_END_NUMBER] = Map[SOURCE_START_NUMBER] + Map[LENGTH] - 1 # -1 because we include the first number
    Map[DESTINATION_END_NUMBER] = Map[DESTINATION_START_NUMBER] + Map[LENGTH] - 1 # -1 because we include the first number
    return Map

'''
Returns an array of conversion tables
'''
def GetListOfMaps(Lines):
    EmptyLineIndexes = [LineIndex for LineIndex, Line in enumerate(Lines) if Line == Lines[SECOND_ITEM]] # The second line of the input will always be empty
    Maps = []
    for Index, EmptyLineIndex in enumerate(EmptyLineIndexes):
        List = []
        if EmptyLineIndex != EmptyLineIndexes[LAST_ITEM]:
            StartIndex = EmptyLineIndexes[Index] + MOVE_UP_2_LINES
            EndIndex = EmptyLineIndexes[Index + NEXT_EMPTY_LINE]
            for Iterator in range(StartIndex, EndIndex):
                Map = CreateMap(Lines[Iterator])
                List.append(Map)
        else:
            StartIndex = EmptyLineIndexes[LAST_ITEM] + MOVE_UP_2_LINES
            for Line in Lines[StartIndex:]:
                Map = CreateMap(Line)
                List.append(Map)
        List = sorted(List, key=lambda o: o[SOURCE_START_NUMBER])
        Maps.append(List)
    return Maps

'''
From a source number and a conversion table, get the destination number
'''
def GetDestination(List, Source):
    for Map in List:
        Start = int(Map[SOURCE_START_NUMBER])
        End = int(Map[SOURCE_START_NUMBER]) + int(Map[LENGTH]) - 1 # -1 because we include the first number
        if Source >= Start and Source <= End:
            Difference = Source - Start
            return int(Map[DESTINATION_START_NUMBER]) + Difference
    return Source

'''
From a destination number and a conversion table, get the source number
'''
def GetSource(List, Destination):
    for Map in List:
        Start = int(Map[DESTINATION_START_NUMBER])
        End = int(Map[DESTINATION_START_NUMBER]) + int(Map[LENGTH]) - 1 # -1 because we include the first number
        if Destination >= Start and Destination <= End:
            Difference = Destination - Start
            return int(Map[SOURCE_START_NUMBER]) + Difference
    return Destination

def recursive(Maps, MapIndex, SourceStart, SourceEnd):
    Locations = []
    OriginalStart = SourceStart
    OriginalEnd = SourceEnd
    while True:
        DestinationStart = SourceStart
        DestinationEnd = SourceEnd
        ClosestStart = SourceEnd
        Found = False
        for Map in Maps[MapIndex]:
            if Map[SOURCE_START_NUMBER] <= SourceStart and Map[SOURCE_END_NUMBER] >= SourceStart:
                Difference = SourceStart - Map[SOURCE_START_NUMBER]
                DestinationStart = Map[DESTINATION_START_NUMBER] + Difference
                if Map[SOURCE_END_NUMBER] < SourceEnd:
                    SourceEnd = Map[SOURCE_END_NUMBER]
                Difference = SourceEnd - Map[SOURCE_START_NUMBER]
                DestinationEnd = Map[DESTINATION_START_NUMBER] + Difference
                Found = True
                break
            else:
                if Map[SOURCE_START_NUMBER] > SourceStart:
                    ClosestStart = min(ClosestStart, Map[SOURCE_START_NUMBER] - 1) # -1 because we dont want to include the source number but the number just before that
        if not Found:
            #check for closest end range
            DestinationEnd = ClosestStart

        if MapIndex != len(Maps) - 1: # -1 because we include the first number
            NewLocations = recursive(Maps, MapIndex + NEXT_NUMBER, DestinationStart, DestinationEnd)
            Locations = Locations + NewLocations
        else:
            Locations.append(DestinationStart)

        #break loop
        SourceEnd = GetSource(Maps[MapIndex], DestinationEnd)
        if SourceEnd == OriginalEnd:
            break
        else:
            SourceStart = SourceEnd + NEXT_NUMBER
            SourceEnd = OriginalEnd
    return Locations

'''
Calculates the answer for part 1 of day 05 of Advent of Code 2023
'''
def Part1(Input):
    with open(Input) as file:
        Lines = file.readlines()

        Seeds = Lines[FIRST_ITEM]
        Seeds = Seeds.split(SEEDS_DELIMITER)[SECOND_ITEM]
        Seeds = Seeds.strip()
        Seeds = Seeds.split(NUMBER_SEPERATOR)

        Maps = GetListOfMaps(Lines)

        Locations = []
        for Seed in Seeds:
            Number = int(Seed)
            for Map in Maps:
                Number = GetDestination(Map, Number)
            Locations.append(Number)

        Answer = min(Locations)
        print(Answer)

'''
Calculates the answer for part 2 of day 05 of Advent of Code 2023
'''
def Part2(Input):
    with open(Input) as file:
        Lines = file.readlines()

        Seeds = Lines[FIRST_ITEM]
        Seeds = Seeds.split(SEEDS_DELIMITER)[SECOND_ITEM]
        Seeds = Seeds.strip()
        Seeds = Seeds.split(NUMBER_SEPERATOR)

        SeedRanges = []
        for Index, Seed in enumerate(Seeds):
            if Index%2 == 0: # every 2 iterations
                Map = {}
                Map[START_NUMBER] = int(Seeds[Index])
                Map[END_NUMBER] = Map[START_NUMBER] + int(Seeds[Index + NEXT_NUMBER]) - 1 # -1 because we include the first number
                SeedRanges.append(Map)
        SeedRanges = sorted(SeedRanges, key=lambda o: o[START_NUMBER])

        Maps = GetListOfMaps(Lines)

        LowestLocation = HIGHEST_VALUE
        for Range in SeedRanges:
            SeedStart = Range[START_NUMBER]
            SeedEnd = Range[END_NUMBER]

            NewLocations = recursive(Maps, FIRST_ITEM, SeedStart, SeedEnd)
            SmallestNewLocation = min(NewLocations)
            LowestLocation = min(LowestLocation, SmallestNewLocation)

        print(LowestLocation)

StartTime = time.time()
#Part1(TEST_INPUT_1_FILE_NAME)
#Part1(INPUT_FILE_NAME)
#Part2(TEST_INPUT_1_FILE_NAME)
#Part2(INPUT_FILE_NAME)
EndTime = time.time()
print("Time: " + str(EndTime - StartTime))