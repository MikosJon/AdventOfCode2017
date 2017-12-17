order = 'a b c d e f g h i j k l m n o p'.split()

instructions = input().strip().split(',')

for instruction in instructions:
    move = instruction[0]
    if move == 's':
        size = int(instruction[1:])
        order = order[-size:] + order[:-size]

    elif move == 'x':
        pos1, pos2 = [int(pos) for pos in instruction[1:].split('/')]
        order[pos1], order[pos2] = order[pos2], order[pos1] 

    elif move == 'p':
        prog1, prog2 = [prog for prog in instruction[1:].split('/')]
        pos1, pos2 = order.index(prog1), order.index(prog2)
        order[pos1], order[pos2] = order[pos2], order[pos1] 

print(''.join(order))
