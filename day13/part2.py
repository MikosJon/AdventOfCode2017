with open('input.txt') as f:
    layers = {}
    severity = 0
    offset = 0

    for line in f:
        line = line.strip().split(': ')

        layers[int(line[0])] = int(line[1])

    while True:
        for level, size in layers.items():
            if (level+offset) % (2*(size-1)) == 0:
                break
        else:
            break
        offset += 1

    print(offset)
