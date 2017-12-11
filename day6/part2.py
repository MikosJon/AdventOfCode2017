# run file as python part2.py
combos = []
search = [1, 0, 14, 14, 12, 11, 10, 9, 9, 7, 5, 5, 4, 3, 7, 1] # the distribution that repeated in part 1
curr = [1, 0, 14, 14, 12, 11, 10, 9, 9, 7, 5, 5, 4, 3, 7, 1]

while True:
    max_val = max(curr)
    index = curr.index(max_val)
    curr[index] = 0
    for i in range(max_val):
        pos = (index+i+1) % len(curr)
        curr[pos] += 1
    if ' '.join(str(a) for a in curr) == ' '.join(str(z) for z in search):
        print(len(combos)+1)
        print(curr)
        break
    else:
        combos.append(' '.join(str(x) for x in curr))
