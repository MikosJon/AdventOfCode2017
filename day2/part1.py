# run file as python part1.py
with open('input.txt') as f:
    count = 0
    for line in f:
        line = line.split()
        max_val = max([int(x) for x in line])
        min_val = min([int(x) for x in line])
        count += max_val - min_val

    print(count)
