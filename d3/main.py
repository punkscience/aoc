f = open("input.txt", "r")
numbers = f.readlines()

EPSILON = 0
GAMMA = 1

def calcRate(numbers, method):
    resultBinary = []
    resultString = ""
    numberLength = len(numbers[0])-1
    totalData = len(numbers)

    # Preallocate an array to count the bits in 1 pass
    for i in range(numberLength):
        resultBinary.append(0)
    
    # For each line, count any bits
    for line in numbers:
        number = line.strip()

        for i, digit in enumerate( number ):
            if method == GAMMA:
                if int( digit ) > 0:
                    resultBinary[i] += 1
            else:
                if int(digit) == 0:
                    resultBinary[i] += 1


   # print( resultBinary )
   # print( totalData / 2)

    # Now translate those into MCB
    for i, digit in enumerate( resultBinary ):
        if digit > totalData / 2:
            resultString += '1' 
        else:
            resultString += '0'

    print( f"Result: {resultString} ({int(resultString,2)})" )

    return int(resultString, 2)
            
gammaRate = calcRate(numbers, GAMMA)
epsilonRate = calcRate(numbers, EPSILON)

result = gammaRate * epsilonRate

print( f"Power Consumption: {result}")



