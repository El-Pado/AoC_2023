
directions = []
nodes = {}
with open( "input", "r" ) as f:
    for i, line in enumerate( f.readlines() ):
        if '=' in line:
            source = line.split('=')[0].strip()
            dest = tuple( line.split('=')[1].strip().replace('(','').replace(')','').replace(',','').split(' ') )
            nodes[source] = dest
        elif line.strip() != '':
            directions = list( line.strip() )

source = 'AAA'
dest   = 'ZZZ'

curr = source
steps = 0
while curr != dest:
    if directions[ steps % len( directions ) ] == 'L':
        curr = nodes[curr][0]
    else:
        curr = nodes[curr][1]
    steps += 1

print( steps )


from math import gcd
def lcm( xs ):
  ans = 1
  for x in xs:
    ans = (x*ans)//gcd(x,ans)
  return ans

currs = [ x for x in nodes if x.endswith('A') ]
steps = 0
steps_loop = {}
while True:
    for i,curr in enumerate( currs ):
        if directions[ steps % len( directions ) ] == 'L':
            curr = nodes[curr][0]
        else:
            curr = nodes[curr][1]
        if curr.endswith('Z'):
            steps_loop[i] = steps+1
        currs[i] = curr
    if len( steps_loop ) == len( currs ):
        break
    steps += 1

print( lcm( steps_loop.values() ) )

# END
