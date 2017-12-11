# run file as python part1.py
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
        if count < 50:
            print(jumps[temp], index, count)
        jumps[temp] += 1
        count += 1
    except IndexError:
        print(count)
        break
