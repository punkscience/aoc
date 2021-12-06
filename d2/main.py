f = open("input.txt", "r")
lines = f.readlines()

depth = 0
hpos = 0
aim = 0

for line in lines:
    words = line.split()
    command = words[0]
    val = int( words[1] )

    if command == 'forward':
        hpos += val
        depth += (aim * val)
    elif command == 'down':
        #depth += val
        aim += val
    elif command == 'up':
        #depth -= val
        aim -= val
    else:
        print( "Unknown command.")

result = depth * hpos

print( f"Result: {result}" )
