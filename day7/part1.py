# run file as python part1.py
nodes = set()
nodesWParent = set()

with open('input.txt') as f:
    for line in f:
        line = line.strip().split('-> ')

        nodes.add(line[0].split()[0])
        if len(line) == 2:
            for node in line[1].split(', '):
                nodesWParent.add(node)
print(nodes - nodesWParent)
