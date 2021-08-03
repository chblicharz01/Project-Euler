"""
Project Euler #12
Chris Blicharz
4-26-2020
"""


#call to find the next triangle number
def newTriNum(inputNum, lastIteration):
    inputNum += (lastIteration+1)
    return(inputNum)

#call to find out the number of divisors in a given number
def findDivisors(inputNum):
    divisors = 0
    for x in range(1, inputNum +1):
        remainder = inputNum % x
        if remainder == 0:
            divisors +=1
    return (divisors)

#number of divisors
divNum = 0 


#starter variables
iterator = 0
currentNum = 1
currentHigh = 0 
#main loop
while divNum < 500:
    iterator += 1
    currentNum = newTriNum(currentNum, iterator)
    divNum = findDivisors(currentNum)
    if divNum > currentHigh:
        print(iterator, '---' ,divNum)
        currentHigh = divNum
print(currentNum, "has", divNum,"divisors")
