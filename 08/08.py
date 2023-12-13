import time
from math import gcd

# File names
INPUT_FILE_NAME = "input.txt"
TEST_INPUT_1_FILE_NAME = "test1.txt"
TEST_INPUT_2_FILE_NAME = "test2.txt"
TEST_INPUT_3_FILE_NAME = "test3.txt"

#Magic Strings
NOTHING = ""

LOCATION_SEPERATOR = "="
DIRECTION_SEPERATOR = ","

OPEN_PARANTHESIS = "("
CLOSE_PARANTHESIS = ")"

STARTING_LOCATION = "AAA"
ENDING_LOCATION = "ZZZ"

ENDS_WITH_A = "A"
ENDS_WITH_Z = "Z"

LEFT = "L"
RIGHT = "R"

#Magic numbers
FIRST_ITEM = 0
SECOND_ITEM = 1
LAST_ITEM = -1

THIRD_LINE = 2
THIRD_LETTER = 2

'''
Calculates the answer for part 1 of day 08 of Advent of Code 2023
'''
def Part1(Input):
    with open(Input) as file:
        Lines = file.readlines()

        Instructions = Lines[FIRST_ITEM][:LAST_ITEM]

        Map = {}
        for Line in Lines[THIRD_LINE:]:
            Line = Line.replace(OPEN_PARANTHESIS,NOTHING).replace(CLOSE_PARANTHESIS,NOTHING)
            Location = Line.split(LOCATION_SEPERATOR)[FIRST_ITEM].strip()
            Left = Line.split(LOCATION_SEPERATOR)[SECOND_ITEM].split(DIRECTION_SEPERATOR)[FIRST_ITEM].strip()
            Right = Line.split(LOCATION_SEPERATOR)[SECOND_ITEM].split(DIRECTION_SEPERATOR)[SECOND_ITEM].strip()
            Map[Location] = {LEFT : Left, RIGHT : Right}

        Location = STARTING_LOCATION
        InstructionCount = 0
        while True:
            LoopInstruction = InstructionCount % len(Instructions)
            Instruction = Instructions[LoopInstruction]
            InstructionCount = InstructionCount + 1
            Location = Map[Location][Instruction]

            if Location == ENDING_LOCATION:
                break

        print(InstructionCount)

'''                 
Calculates the answer for part 2 of day 08 of Advent of Code 2023
'''
def Part2(Input):
    with open(Input) as file:
        Lines = file.readlines()

        Instructions = Lines[FIRST_ITEM][:LAST_ITEM]

        Nodes = []
        Map = {}
        for Line in Lines[THIRD_LINE:]:
            Line = Line.replace(OPEN_PARANTHESIS, NOTHING).replace(CLOSE_PARANTHESIS, NOTHING)
            Location = Line.split(LOCATION_SEPERATOR)[FIRST_ITEM].strip()
            Left = Line.split(LOCATION_SEPERATOR)[SECOND_ITEM].split(DIRECTION_SEPERATOR)[FIRST_ITEM].strip()
            Right = Line.split(LOCATION_SEPERATOR)[SECOND_ITEM].split(DIRECTION_SEPERATOR)[SECOND_ITEM].strip()
            Map[Location] = {LEFT: Left, RIGHT: Right}
            if Location[THIRD_LETTER] == ENDS_WITH_A:
                Nodes.append(Location)

        InstructionCount = 0
        Loops = {}
        while len(Loops) != len(Nodes):
            LoopInstruction = InstructionCount % len(Instructions)
            Instruction = Instructions[LoopInstruction]
            InstructionCount = InstructionCount + 1
            NewNodes = []
            for Index, Node in enumerate(Nodes):
                Location = Map[Node][Instruction]
                if Location[THIRD_LETTER] == ENDS_WITH_Z:
                    if not Index in Loops:
                        Loops[Index] = InstructionCount
                NewNodes.append(Location)
            Nodes = NewNodes

        lcm = 1
        for i in list(Loops.values()):
            lcm = lcm * i // gcd(lcm, i)
        print(lcm)

StartTime = time.time()
#Part1(TEST_INPUT_1_FILE_NAME)
#Part1(TEST_INPUT_2_FILE_NAME)
#Part1(INPUT_FILE_NAME)
#Part2(TEST_INPUT_3_FILE_NAME)
#Part2(INPUT_FILE_NAME)
EndTime = time.time()
print("Time: " + str(EndTime - StartTime))