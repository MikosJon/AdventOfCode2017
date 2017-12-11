# run file as python part1.py
with open('input.txt') as f:
    count = 0
    for line in f:
        line = line.split()
        if len(line) == len(set(line)):
            count += 1


    print(count)
