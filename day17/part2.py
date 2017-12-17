steps = int(input().strip())

pos = 0
valAfter0 = 0

for val in range(1, 50000001):
    if val % 100000 == 0:
        print(val)
    pos = (pos + steps + 1) % val
    if pos == 0:
        valAfter0 = val

print(valAfter0)
