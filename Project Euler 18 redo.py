fake =  \
"""
75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
"""

#call to get rid of spaces in the prymid
def remove(string): 
    return string.replace(" ", "")

prymid = remove(fake)

lastPos = 0
currentLine = ""
op1 = 0
op2 = 0
total = int(prymid[1]+ prymid[2])

for x in range(4, len(prymid)): #cycles through the pyrmid digit by digit
    if prymid[x] !='\n':
        currentLine += prymid[x]
    elif prymid[x] == '\n':
        if int(currentLine[lastPos]) == 0:
            op1 = int(currentLine[lasPos+1])
        else:           
            op1 = int(currentLine[lastPos] + currentLine[lastPos+1])
        if int(currentLine[lastPos+2]) == 0:
            op2 = int(currentLine[lastPos +3])
        else:
            op2 = int(currentLine[lastPos+2] + currentLine[lastPos+3])
        if op1 < op2:
            lastPos += 2
            total += op2
        else:
            total += op1
        currentLine = ""


print("The total is: ", total)
input("Press enter to exit:")
            
            
        
    
