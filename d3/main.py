
EPSILON = 0
GAMMA = 1
OXYGEN = 3
CO2 = 4

MCV = 0
LCV = 1


def processData( raw ):
    data = []

    # Clean house
    for index, line in enumerate( raw ):
        line = line.strip()

        bits = []

        for char in line:
            if char == "1":
                bits.append( 1 )
            else:
                bits.append( 0 )

        data.append( bits )

    return data


def detectMostCommonValue( dataList, position ):
    oneCount = 0
    totalData = len(dataList)

    for number in dataList: 
        if number[position] == '1':
            oneCount += 1

    if oneCount >= (totalData/2):
        return 1
    
    return 0


def getCommonValueCriteria( data ):
    numberLen = len(data[0])
    counts = []
    criteria = []

    for i in range( numberLen ):
        counts.append( 0 )
        for number in data:
            if number[i] == 1:
                counts[i] += 1

    majority = len(data) / 2
   
    for i in counts:
        if i >= majority:
            criteria.append( 1 )
        else:
            criteria.append( 0 )

    return criteria


def calcLSRate( data, method ):
    criteriaList = getCommonValueCriteria(data)
    criteriaLen = len( criteriaList )
    
    print( f"Criteria: {criteriaList}")

    # Test against all the criteria
    for i in range( criteriaLen ):
        criteria = criteriaList[i]

        # Flip the meaning for CO2
        if method == CO2:
            criteria = 1 - criteria

        data = filter(data, criteria, i )
       
        if len( data ) == 1:
            break

        # Convert it to a string so we can later convert it to a binary number
        string_ints = [str(int) for int in data[0]]
        str_of_ints = "".join(string_ints)

    return str_of_ints

  
def filter( numbers, criteria, position ):
    filtered = []

    for number in numbers:
        if int( number[position]) == criteria:
            filtered.append( number )

    return filtered


def calcRate(numbers, method):
    resultBinary = []
    resultString = ""
    numberLength = len(numbers[0])
    totalData = len(numbers)

    # Preallocate an array to count the bits in 1 pass
    for i in range(numberLength):
        resultBinary.append(0)
    
    # For each line, count any bits
    for number in numbers:
        for i, digit in enumerate( number ):
            if method == GAMMA:
                if int( digit ) > 0:
                    resultBinary[i] += 1
            else:
                if int(digit) == 0:
                    resultBinary[i] += 1


    # Now translate those into MCB
    for i, digit in enumerate( resultBinary ):
        if digit > totalData / 2:
            resultString += '1' 
        else:
            resultString += '0'

    print( f"Result: {resultString} ({int(resultString,2)})" )

    return resultString
            

f = open("input.txt", "r")
lines = f.readlines()
data = processData( lines )


gammaRate = int( calcRate(data, GAMMA), 2 )
epsilonRate = int( calcRate( data, EPSILON), 2 )
oxygenRate = int( calcLSRate( data, OXYGEN ), 2)
c02Rate = int( calcLSRate( data, CO2 ), 2)

result = gammaRate * epsilonRate
lifeSupport = oxygenRate * c02Rate

print( f"Power Consumption: {result}")
print(f"Life Support: {lifeSupport}")



