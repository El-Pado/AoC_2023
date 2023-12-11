
grid = {}
start = (0,0)
imax = 0
jmax = 0
with open( "input", "r" ) as f:
    for i, line in enumerate( f.readlines() ):
        imax = i
        for j, v in enumerate( list( line.strip() ) ):
            jmax = j
            grid[(i,j)] = v
            if v == 'S':
                start = (i,j)

def left( p ):
    (i,j) = p
    return (i,j-1)
def right( p ):
    (i,j) = p
    return (i,j+1)
def up( p ):
    (i,j) = p
    return (i-1,j)
def down( p ):
    (i,j) = p
    return (i+1,j)

def get_next_tile( prev, curr ):
    c = grid[curr]
    if prev == left( curr ):
        if c == '-': return right( curr )
        if c == '7': return down( curr )
        if c == 'J': return up( curr )
    if prev == right( curr ):
        if c == '-': return left( curr )
        if c == 'F': return down( curr )
        if c == 'L': return up( curr )
    if prev == up( curr ):
        if c == '|': return down( curr )
        if c == 'L': return right( curr )
        if c == 'J': return left( curr )
    if prev == down( curr ):
        if c == '|': return up( curr )
        if c == 'F': return right( curr )
        if c == '7': return left( curr )

tiles = []
start_symb = []
if start[1] > 0 and grid[ left( start ) ] in ['-','F','L']:
    tiles.append( left( start ) )
    start_symb.append( ['-','J','7'] )
if start[1] < jmax and grid[ right( start ) ] in ['-','J','7']:
    tiles.append( right( start ) )
    start_symb.append( ['-','F','L'] )
if start[0] > 0 and grid[ up( start ) ] in ['|','F','7']:
    tiles.append( up( start ) )
    start_symb.append( ['|','J','L'] )
if start[0] < imax and grid[ down( start ) ] in ['|','J','L']:
    tiles.append( down( start ) )
    start_symb.append( ['|','F','7'] )

tiles[0] = [ start, tiles[0] ]
tiles[1] = [ start, tiles[1] ]

steps = 1
while tiles[0][-1] != tiles[1][-1]:
    steps += 1
    for i in [0,1]:
        tiles[i].append( get_next_tile( tiles[i][-2], tiles[i][-1] ) )

print( steps )

grid[start] = list( set( start_symb[0] ).intersection( set( start_symb[1] ) ) )[0]

outsides = []
insides = []
inside = False
for i in range( imax+1 ):
    inside = False
    line = ''
    for j in range( jmax+1 ):
        line += grid[(i,j)]
    for j in range( jmax ):
        if (i,j) in tiles[0] + tiles[1]:
            nj = j+1
            while nj < jmax and grid[(i,nj)] == '-':
                nj += 1
            if grid[(i,j)] == '|':
                inside = not inside
            elif grid[(i,j)] == 'F' and grid[(i,nj)] == 'J':
                inside = not inside
            elif grid[(i,j)] == 'L' and grid[(i,nj)] == '7':
                inside = not inside
        else:
            if inside: insides.append( (i,j) )
            else: outsides.append( (i,j) )

print( len( insides ) )

if False:
    for i in range( imax+1 ):
        line = ''
        for j in range( jmax+1 ):
            line += grid[(i,j)]
        print( line )
    print()
    for p in insides:
        grid[p] = 'I'
    for p in outsides:
        grid[p] = 'O'
    for i in range( imax+1 ):
        line = ''
        for j in range( jmax+1 ):
            line += grid[(i,j)]
        print( line )

# END
