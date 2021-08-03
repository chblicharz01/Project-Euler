num = 1
total = 0
limit = 10001
printVar = 0
while total < limit:
    num += 1
    tester = bool(False) #false means that the number is prime/ true means the number is NOT prime
    for x in range (2, num):
            remainder = num % x
            if remainder == 0:
                tester = True
    if tester == False:
        printVar = num
        print(num)
        total += 1

input("Press Enter to Exit")



    
