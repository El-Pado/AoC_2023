
galaxies = []
with open( "input", "r" ) as f:
    for i, line in enumerate( f.readlines() ):
        for j, c in enumerate( list( line.strip() ) ):
            if c == '#':
                galaxies.append ( (i,j) )

galaxies_rows = set( [ x[0] for x in galaxies ] )
galaxies_cols = set( [ x[1] for x in galaxies ] )

new_galaxies = []
def solve( expansion_factor ):
    new_galaxies = []
    for g in galaxies:
        g0 = g[0] + ( expansion_factor - 1 ) * ( g[0] - len( set( range( g[0] ) ).intersection( galaxies_rows ) ) )
        g1 = g[1] + ( expansion_factor - 1 ) * ( g[1] - len( set( range( g[1] ) ).intersection( galaxies_cols ) ) )
        new_galaxies.append( (g0,g1) )

    length = 0
    for i, g1 in enumerate( new_galaxies ):
        for g2 in new_galaxies[i+1:]:
            length += abs( g2[0]-g1[0] ) + abs( g2[1]-g1[1] )
    return length

expansion_factor = 2
length = solve( expansion_factor )
print( length )

expansion_factor = 1000000
length = solve( expansion_factor )
print( length )

if False:
    for i in range( max( [ x[0] for x in new_galaxies ] ) + 1 ):
        line = ''
        for j in range( max( [ x[1] for x in new_galaxies ] ) + 1 ):
            if (i,j) in new_galaxies:
                line += '#'
            else:
                line += '.'
        print( line )

# END
