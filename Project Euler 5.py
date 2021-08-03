num = 232792559
while True:
    num += 1
    tester = bool(True)
    for x in range (17):
        remainder= num % (x + 1)
        if remainder != 0:
            tester = False
    if tester == True:
        break

print("Smallest divisible number is ", num)
        

    

    
