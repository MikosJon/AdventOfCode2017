# run file as python part1.py
from collections import defaultdict, deque

with open('input.txt') as f:
    connections = defaultdict(list)
    for line in f:
        line = line.strip().split(' <-> ')
        
        for node in line[1].split(', '):
            connections[line[0]].append(node)

    visited = []
    queue = deque([node for node in connections['0']])
    while queue: 
        curr = queue.pop()
        if curr not in visited:
            visited.append(curr)
            queue.extend([neighbour for neighbour in connections[curr]])

    print(len(visited))
