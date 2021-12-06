f = open("input.txt", "r")
numbers = f.readlines()

EPSILON = 0
GAMMA = 1
OXYGEN = 3
CO2 = 4

def detectMostCommonValue( numbers, position ):
    bits = 0
    numberLen = len(numbers)

    for line in numbers:
        number = line.strip()
        
        if number[position] == '1':
            bits += 1

    if bits >= (numberLen/2):
        return 1
    
    return 0


def calcLSRate( numbers, method ):
    numberLen = len(numbers[0].strip())
    resultList = numbers.copy()

    # Test against all the criteria
    for i in range(numberLen):
        criteria = detectMostCommonValue(numbers, i)

        # Flip the meaning for CO2
        if method == CO2:
            if criteria == 1:
                criteria = 0
            else:
                criteria = 1

        resultList = filter(resultList, criteria, i )

        if len(resultList) == 1:
            return resultList[0]

    return calcLSRate( resultList, method )


def filter( numbers, criteria, position ):
    resultList = numbers.copy()

    for line in resultList:
        number = line.strip()

        print( f"number: {number[position]} criteria: {criteria}")
        if number[position] != str(criteria):
            print( f"Removed {line}")
            resultList.remove(line)

    return resultList



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

    return resultString
            
gammaRate = int( calcRate(numbers, GAMMA), 2 )
epsilonRate = int( calcRate(numbers, EPSILON), 2 )
oxygenRate = int( calcLSRate( numbers, OXYGEN ), 2)
c02Rate = int( calcLSRate( numbers, CO2 ), 2)

result = gammaRate * epsilonRate
lifeSupport = oxygenRate * c02Rate

print( f"Power Consumption: {result}")
print(f"Life Support: {lifeSupport}")



