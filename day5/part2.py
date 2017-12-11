# run file as python part2.py
count = 0
index = 0
jumps = []

with open('input.txt') as f:
    for line in f:
        jumps.append(int(line))

while True:
    try:
        temp = index
        index += jumps[index]
        if index < 0:
            print(count)
            break
        if jumps[temp] < 3:
            jumps[temp] += 1
        else:
            jumps[temp] -= 1
        count += 1
    except IndexError:
        print(count)
        break
