"""
Project Euler: Problem 17
Chris Blicharz
4/11/2020
"""

answer = int(0) 

#call to remove spaces
def remove(string): 
    return string.replace(" ", "")

#word library
ones = ["", "one ","two ","three ","four ", "five ",\
        "six ","seven ","eight ","nine ","ten ","eleven ", \
        "twelve ", "thirteen ", "fourteen ", "fifteen ","sixteen ",\
        "seventeen ", "eighteen ","nineteen "]
tens = ["","","twenty ","thirty ","forty ", "fifty ",\
        "sixty ","seventy ","eighty ","ninety "]

#call to change a number into a string of the words 
def numToWord(num):
    numLen= len(str(num))
    string = ""
    if num < 20:
        string = ones[num]
    elif num < 100:
        string += (tens[int(str(num)[0])] + ones[int(str(num)[1])])
    elif num <1000:
        string += ((ones[int(str(num)[0])]) + "hundred")
        if int((str(num)[1]) + (str(num)[2])) < 20 and int((str(num)[1]) + (str(num)[2])) != 0:
            string += "and" + ones[int((str(num)[1]) + (str(num)[2]))]
        elif int((str(num)[1]) + (str(num)[2])) != 0:
            string += "and" + (tens[int(str(num)[1])] + ones[int(str(num)[2])])
    return string

for x in range (1,(1001)):
    chapter = numToWord(x)
    answer += len(remove(chapter))
    print(remove(chapter))
print("onethousand")
answer += len(str("onethousand"))
print("The number of characters used is: ", answer)





