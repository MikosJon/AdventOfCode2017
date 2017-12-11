# run file as python part2.py
with open('input.txt') as f:
    count = 0
    for line in f:
        line = line.split()
        temp = []
        for phrase in line:
            temp.append(''.join(sorted(phrase)))
        if len(temp) == len(set(temp)):
            count += 1

    print(count)
