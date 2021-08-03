"""
Project Euler 18
Chris Blicharz
4-13-2020
"""
#call to get rid of spaces in the prymid
def remove(string): 
    return string.replace(" ", "")
rawString = \
"""
3
7 4
2 4 6
8 5 9 3
"""
#copy and paste the prymid here/this is the string variable

prymid = remove(rawString)

#used later to give the string of a line
currentLine = ""

position = 0
op1 = 0
op2 = 0

total = 0 
currentHighest = 0

numOfRows = int(4)
prymidLen = len(prymid)

        
        
    
for x in range(1, prymidLen):
    if (prymid[x]) == '\n':
        print(currentLine)
        print("New Line")
        currentLine = ""
    else:
        currentLine += (prymid[x])

            
        
   
    
