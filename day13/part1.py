with open('input.txt') as f:
    layers = {}
    severity = 0

    for line in f:
        line = line.strip().split(': ')

        layers[int(line[0])] = int(line[1])

    for level, size in layers.items():
        if level % (2*(size-1)) == 0:
            severity += level*size

    print(severity)
