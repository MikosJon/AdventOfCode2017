# run file as python part1.py
combos = []
curr = []

with open('input.txt') as f:
    for line in f:
        curr = [int(x) for x in line.split()]

while True:
    max_val = max(curr)
    index = curr.index(max_val)
    curr[index] = 0
    for i in range(max_val):
        pos = (index+i+1) % len(curr)
        curr[pos] += 1
    if ' '.join(str(a) for a in curr) in combos:
        print(len(combos)+1)
        print(curr)
        break
    else:
        combos.append(' '.join(str(x) for x in curr))
