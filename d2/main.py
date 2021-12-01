
def ReadData( filename ):
    readings = []

    with open( filename, "r" ) as f:
        lines = f.readlines()
        
        for line in lines:
            readings.append( int( line.strip() ) )

    return readings


data = ReadData( '../input.txt' )

previous = data[0]
increase_count = 0
frame_index = 0

for sample in data:
    if sample > previous:
        increase_count = increase_count + 1
    previous = sample

print( f'There have been {increase_count} progressions.')



