from collections import defaultdict

def cleanNode():
    return '.'

grid = defaultdict(cleanNode)
x = 12 # the start grid is 25x25 => the virus starts in the middle at node (12, 12)
y = 12
idx_direction = 0 # directions = 'NESW'

with open('input.txt') as f:
    for idx, line in enumerate(f):
        line = line.strip()
        for i, node in enumerate(line):
            grid[(idx, i)] = node

num_infections = 0
for burst in range(10000):
    if grid[(x, y)] == '.':
        idx_direction = (idx_direction - 1) % 4
        grid[(x, y)] = '#'
        num_infections += 1
    else:
        idx_direction = (idx_direction + 1) % 4
        grid[(x, y)] = '.'
        
    if idx_direction == 0:
        x -= 1
    elif idx_direction == 1:
        y += 1
    elif idx_direction == 2:
        x += 1
    elif idx_direction == 3:
        y -= 1

print(num_infections)
