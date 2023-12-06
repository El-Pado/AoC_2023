
total_worth = 0
with open( "input", "r") as f:
       nb_cards = sum(1 for _ in f)

stack = [1,]*nb_cards
with open( "input", "r" ) as f:
    for i, line in enumerate( f.readlines() ):
        worth = 0
        count = 0
        winning = [ int(x) for x in line.split('|')[0].split(':')[1].strip().split(' ') if x != '' ]
        numbers = [ int(x) for x in line.split('|')[1].strip().split(' ') if x != '' ]
        for n in numbers:
            if n in winning:
                count += 1
                worth = max( 1, worth * 2 )
                stack[i+count] += stack[i]
        total_worth += worth

print( total_worth )
print( sum( stack ) )

# END
