y = 999
product = 0
productS = ""
currentL = 0
backwardS = ""
lenString = 0 
for x in range (999, 0, -1):
    for y in range (999, 0, -1):
        product =  x * y
        productS = str(product)
        lenString = len(str(product))
        backwardS = ""
        for z in productS:
            backwardS += productS[lenString-1]
            lenString -= 1
        if backwardS == productS:
            if product > currentL:
                currentL = product
                
            
print("Largest palindrome is ", currentL)

input("Press enter to exit")
        
            
            
