# run file as python part2.py
from collections import defaultdict, deque

with open('input.txt') as f:
    connections = defaultdict(list)
    for line in f:
        line = line.strip().split(' <-> ')
        
        for node in line[1].split(', '):
            connections[line[0]].append(node)

    numGroups = 0
    visited = []
    for cell in connections.keys():
        if cell not in visited:
            numGroups += 1
            queue = deque([node for node in connections[cell]])
            while queue: 
                curr = queue.pop()
                if curr not in visited:
                    visited.append(curr)
                    queue.extend([neighbour for neighbour in connections[curr]])

    print(numGroups)
