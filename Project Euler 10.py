
#call to determine if the given number is prime or not
def testPrime(number):
    for x in range(2, int(number/2)+1):
        remainder = number % x
        if remainder == 0:
            return True
            break
    return False
        
total = 2
lastNum = int(input("Enter a postive integer as the limit for the summation: "))
status = bool(False)

for x in range(3, lastNum +1):
    status = testPrime(x)
    if status == False:
        total += x
    status = False
    if x == int(1000000):
        print("Halfway there!!")
    if x == int(500000):
        print("Quarter of the way...")
    if x == int(15000000):
        print("Three quarters there...")
    if x == 1900000:
        print("Only 100,000 to go!!!")
        


print("The summation of primes below", lastNum,"is",total)

input("Press enter to exit...")
