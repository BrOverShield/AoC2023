import time

# File names
INPUT_FILE_NAME = "input.txt"
TEST_INPUT_1_FILE_NAME = "test1.txt"

#Magic Numbers
NONE = 0
FIRST_NUMBER = 1

FIRST_ITEM  = 0
SECOND_ITEM = 1

#Magic Strings
NOTHING = ""
SPACE = " "
TITLE_DELIMITER = ":"

'''
Calculates the answer for part 1 of day 06 of Advent of Code 2023
'''
def Part1(Input):
    with open(Input) as file:
        Lines = file.readlines()

        Times = Lines[FIRST_ITEM].split(TITLE_DELIMITER)[SECOND_ITEM]
        Times = SPACE.join(Times.split())
        Times = Times.split(SPACE)
        Times = [int(Time) for Time in Times ]

        Distances = Lines[SECOND_ITEM].split(TITLE_DELIMITER)[SECOND_ITEM]
        Distances = SPACE.join(Distances.split())
        Distances = Distances.split(SPACE)
        Distances = [int(Distance) for Distance in Distances]

        Answer = 1 # 1 because we multiply

        for Index, Time in enumerate(Times):
            Possibilities = NONE
            for Milliseconds in range(FIRST_NUMBER, Time + 1): # +1 because range does not include the last number
                TimeLeft = Time - Milliseconds
                Distance = TimeLeft * Milliseconds
                if Distance > Distances[Index]:
                    Possibilities = Possibilities + 1
            Answer = Answer * Possibilities

        print(Answer)


'''
Calculates the answer for part 2 of day 06 of Advent of Code 2023
'''
def Part2(Input):
    with open(Input) as file:
        Lines = file.readlines()

        Time = Lines[FIRST_ITEM].split(TITLE_DELIMITER)[SECOND_ITEM]
        Time = SPACE.join(Time.split())
        Time = Time.replace(SPACE,NOTHING)
        Time = int(Time)

        TargetDistance = Lines[SECOND_ITEM].split(TITLE_DELIMITER)[SECOND_ITEM]
        TargetDistance = SPACE.join(TargetDistance.split())
        TargetDistance = TargetDistance.replace(SPACE, NOTHING)
        TargetDistance = int(TargetDistance)

        Answer = NONE

        for Milliseconds in range(FIRST_NUMBER, Time + 1): # +1 because range does not include the last number
            TimeLeft = Time - Milliseconds
            Distance = TimeLeft * Milliseconds
            if Distance > TargetDistance:
                Answer = Answer + 1

        print(Answer)

StartTime = time.time()
#Part1(TEST_INPUT_1_FILE_NAME)
#Part1(INPUT_FILE_NAME)
#Part2(TEST_INPUT_1_FILE_NAME)
#Part2(INPUT_FILE_NAME)
EndTime = time.time()
print("Time: " + str(EndTime - StartTime))