
next_values = []
prev_values = []
with open( "input", "r" ) as f:
    for line in f.readlines():
        s = []
        s.append( [ int(x) for x in line.strip().split(' ') if x != '' ] )
        while s[-1] != [0,]*len(s[-1]):
            s.append( [ s[-1][i+1]-s[-1][i] for i in range( len(s[-1])-1 ) ] )
        next_values.append( sum( [ s[i][-1] for i in range( len(s) ) ] ) )
        prev_values.append( sum( [ s[i][0] for i in range( len(s) ) if i%2 == 0 ] + [ -s[i][0] for i in range( len(s) ) if i%2 == 1 ] ) )

print( sum( next_values ) )
print( sum( prev_values ) )

# END
