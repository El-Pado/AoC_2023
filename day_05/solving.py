
seeds = []
maps = []
with open( "input", "r" ) as f:
    for i, line in enumerate( f.readlines() ):
        if line.startswith( "seeds" ):
            seeds = [ int(x) for x in line.split(':')[1].strip().split(' ') if x != '' ]
        if "map" in line:
            maps.append( [] )
        if line[0].isdigit():
            maps[-1].append( [ int(x) for x in line.split(' ') if x != '' ] )

locations = []
for s in seeds:
    for m in maps:
        for [dest_start, source_start, range_length] in m:
            if source_start <= s and s < source_start+range_length:
                s += dest_start - source_start
                break
    locations.append( s )

print( min( locations ) )


def func(e):
    return e[1]

s = seeds
for m in maps:
    m.sort( key=func )
    s2 = []
    for i in range( len( s ) ):
        if i%2 == 0:
            start = s[i]
            rang = s[i+1]
            for [dest_start, source_start, range_length] in m:
                if start < source_start:
                    s2.append( start )
                    s2.append( min( source_start-start, rang ) )
                    start = s2[-2]+s2[-1]+1
                    rang = s[i]+s[i+1]-start
                if source_start <= start and start < source_start+range_length:
                    s2.append( start + dest_start - source_start )
                    s2.append( min( dest_start+range_length-s2[-1], rang ) )
                    start = start+s2[-1]
                    rang = s[i]+s[i+1]-start
                if rang == 0:
                    break
            if rang > 0:
                s2.append( start )
                s2.append( rang )
    s = s2
    s2 = []

print( min( [ x for i,x in enumerate(s) if i%2 == 0 ] ) )

# END
