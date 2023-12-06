
times = []
distances = []
with open( "input", "r" ) as f:
    for i, line in enumerate( f.readlines() ):
        if line.startswith( "Time" ):
            times = [ int(x) for x in line.split(':')[1].strip().split(' ') if x != '' ]
            time = int( line.split(':')[1].strip().replace(' ','') )
        if line.startswith( "Distance" ):
            distances = [ int(x) for x in line.split(':')[1].strip().split(' ') if x != '' ]
            distance = int( line.split(':')[1].strip().replace(' ','') )

margin = 1
for race in range( len( times ) ):
    wins = 0
    for duration in range( times[race] ):
        dist = duration * ( times[race] - duration )
        if dist > distances[race]:
            wins += 1
    margin = margin * wins

print( margin )

wins = 0
for duration in range( time ):
    dist = duration * ( time - duration )
    if dist > distance:
        wins += 1

print( wins )

# END
