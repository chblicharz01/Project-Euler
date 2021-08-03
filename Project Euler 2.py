total = 2
p1Num = 1
p2Num = 2
currentNum = 3
while True:
    if currentNum < 4000000:
        currentNum = p1Num + p2Num
        test = currentNum % 2
        if test == 0:
            total += currentNum
            p1Num = p2Num
            p2Num = currentNum
        else:
            p1Num = p2Num
            p2Num = currentNum
    else:
        print(total)
        break

input("Press Enter to Exit...")

            
            
