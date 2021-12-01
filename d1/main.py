
with open('./input.txt', "r" ) as f:
    lines = f.readlines()

    increases = 0
    previous = int( lines[0].strip() )

    for line in lines:
        number = int( line.strip() )
        if number > previous:
            increases = increases + 1
        previous = number
    
    print( f'There have been {increases} progressions.')



