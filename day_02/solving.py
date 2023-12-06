
mins = {
        "red":12,
        "green":13,
        "blue":14
        }

games_ok = 0
powers = []
games = []
cubes = {}
with open( "input", "r" ) as f:
    for i, line in enumerate( f.readlines() ):
        game_ok = [True,]*3
        min_set = [0,]*3
        cubes["red"] = []
        cubes["green"] = []
        cubes["blue"] = []
        for subset in line.split(':')[-1].split(';'):
            for j, key in enumerate( cubes ):
                val = [ x.strip().split(' ')[0] for x in subset.split(',') if key in x ]
                if val:
                    cubes[key].append( int(val[0]) )
                    min_set[j] = max( min_set[j], int(val[0]) )
                    if int(val[0]) > mins[key]:
                        game_ok[j] = False
        powers.append( min_set[0]*min_set[1]*min_set[2] )
        if not False in game_ok:
            games_ok += i+1
        games.append( cubes )

print( games_ok )
print( sum( powers ) )

# END
