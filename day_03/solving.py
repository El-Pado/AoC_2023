
s = []
with open( "input", "r" ) as f:
    for i, line in enumerate( f.readlines() ):
        s.append( list( line.strip() ) )

def look_for_symbol( i, j ):
    for di in [-1,0,1]:
        for dj in [-1,0,1]:
            i2 = min( len( s )   -1, max( 0, i+di ) )
            j2 = min( len( s[0] )-1, max( 0, j+dj ) )
            if not s[i2][j2].isdigit() and s[i2][j2] != '.':
                return (i2, j2)
    return False

parts_sum = 0
number = ''
symbol = ''
is_part_nb = False
symbols = {}
for i in range( len( s ) ):
    if is_part_nb:
        parts_sum += int( number )
        if symbol in symbols:
            symbols[symbol].append(int( number ) )
        else:
            symbols[symbol] = [ int( number ) ]
    number = ''
    is_part_nb = False
    for j in range( len( s ) ):
        if s[i][j].isdigit():
            number += s[i][j]
            if look_for_symbol( i, j ):
                symbol = look_for_symbol( i, j )
                is_part_nb = True
        else:
            if is_part_nb:
                parts_sum += int( number )
                if symbol in symbols:
                    symbols[symbol].append(int( number ) )
                else:
                    symbols[symbol] = [ int( number ) ]
            number = ''
            is_part_nb = False

ratio_sum = 0
for symbol in symbols:
    i = int( symbol[0] )
    j = int( symbol[1] )
    if s[i][j] == '*' and len( symbols[symbol] ) == 2:
        ratio_sum += symbols[symbol][0]*symbols[symbol][1]

print( parts_sum )
print( ratio_sum )

# END
