
calib = []
with open( "input", "r" ) as f:
    for line in f.readlines():
        ints = list( filter( lambda x: x.isdigit(), list( line ) ) )
        calib.append( int( ints[0] + ints[-1] ) )
print( sum( calib ) )

reps = {
    'one':'1',
    'two':'2',
    'three':'3',
    'four':'4',
    'five':'5',
    'six':'6',
    'seven':'7',
    'eight':'8',
    'nine':'9'
}

calib = []
with open( "input", "r" ) as f:
    for line in f.readlines():
        ints = []
        for i in range( len( line ) ):
            if line[i].isdigit():
                ints.append( line[i] )
            for key in reps:
                if line[i:].startswith( key ):
                    ints.append( reps[key] )
        calib.append( int( ints[0] + ints[-1] ) )
print( sum( calib ) )

# END
