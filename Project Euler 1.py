total = 0
counter = 0
while True:
    if counter < 1000:
        test = counter % 3
        test5 = counter % 5 
        if test == 0:
            total += counter
            counter +=1
        elif test5 == 0:
            total += counter
            counter +=1
        else:
            total += 0
            counter +=1
    else:
        print(total)
        break

input("Press enter to exit...")
            
            
