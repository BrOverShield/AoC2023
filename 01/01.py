with open('input.txt') as file:
    Lines = file.readlines()
    
    Answer = 0
    
    # for each line of thee input
    for Line in Lines:
    
        # Find the first number in the string
        FirstNumber = 0
        for Character in Line:
            if Character.isdigit():
                FirstNumber = Character
                break
                
        #Reverse the string
        ReversedLine = Line[::-1]
        
        # Find the first number in the string
        LastNumber = 0
        for Character in ReversedLine:
            if Character.isdigit():
                LastNumber = Character
                break
        
        # Combine the two numbers
        Combination = str(FirstNumber) + str(LastNumber)
        
        Answer = Answer + int(Combination)
        
    print(Answer)