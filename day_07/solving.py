
hands = []
with open( "input", "r" ) as f:
    for i, line in enumerate( f.readlines() ):
        hands.append( tuple( line.strip().split(' ') ) )

types = {}
types["five"]  = []
types["four"]  = []
types["full"]  = []
types["three"] = []
types["two"]   = []
types["one"]   = []
types["high"]  = []

for hand in hands:
    h = list( hand[0] )
    cards = list( set( h ) )
    counts = [ h.count( cards[i] ) for i in range( len( set( h ) ) ) ]
    if 5 in counts:
        types["five"].append( hand )
    elif 4 in counts:
        types["four"].append( hand )
    elif 3 in counts and 2 in counts:
        types["full"].append( hand )
    elif 3 in counts:
        types["three"].append( hand )
    elif counts.count(2) == 2:
        types["two"].append( hand )
    elif 2 in counts:
        types["one"].append( hand )
    else:
        types["high"].append( hand )

def func( e ):
    tot = 0
    for i in range( len( e[0] ) ):
        f = e[0][i]
        if f == 'T': r = 10
        elif f == 'J': r = 11
        elif f == 'Q': r = 12
        elif f == 'K': r = 13
        elif f == 'A': r = 14
        else: r = int(f)
        tot += r * pow( 100, ( len( e[0] ) - i ) )
    return tot

ranks = []
for t in "high", "one", "two", "three", "full", "four", "five":
    types[t].sort( key = func )
    ranks += types[t]

winnings = 0
for i in range( len( ranks ) ):
    winnings += (i+1)*int(ranks[i][1])

print( winnings )


types = {}
types["five"]  = []
types["four"]  = []
types["full"]  = []
types["three"] = []
types["two"]   = []
types["one"]   = []
types["high"]  = []

for hand in hands:
    h = list( hand[0] )
    cards = list( set( h ) )
    counts = [ h.count( cards[i] ) for i in range( len( set( h ) ) ) if cards[i] != 'J' ]
    if 2 in counts:
        counts2 = list( counts )
        counts2.remove( 2 )
    count_j = h.count( 'J' )
    if count_j == 5:
        types["five"].append( hand )
    elif 5-count_j in counts:
        types["five"].append( hand )
    elif 4-count_j in counts:
        types["four"].append( hand )
    elif 3 in counts and 2-count_j in counts:
        types["full"].append( hand )
    elif 2 in counts and 3-count_j in counts2:
        types["full"].append( hand )
    elif 3-count_j in counts:
        types["three"].append( hand )
    elif 2 in counts and 2-count_j in counts2:
        types["two"].append( hand )
    elif 2-count_j in counts:
        types["one"].append( hand )
    else:
        types["high"].append( hand )

def func2( e ):
    tot = 0
    for i in range( len( e[0] ) ):
        f = e[0][i]
        if f == 'T': r = 10
        elif f == 'J': r = 1
        elif f == 'Q': r = 12
        elif f == 'K': r = 13
        elif f == 'A': r = 14
        else: r = int(f)
        tot += r * pow( 100, ( len( e[0] ) - i ) )
    return tot

ranks = []
for t in "high", "one", "two", "three", "full", "four", "five":
    types[t].sort( key = func2 )
    ranks += types[t]

winnings = 0
for i in range( len( ranks ) ):
    winnings += (i+1)*int(ranks[i][1])

print( winnings )

# END
