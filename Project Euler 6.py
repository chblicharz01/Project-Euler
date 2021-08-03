num = 100
total = 0
sumTot = 0
for x in range (num):
    total += ((x + 1)**2 )

for x in range (num +1):
    sumTot += x

squareSum = (sumTot ** 2)

print(squareSum -  total)
    
