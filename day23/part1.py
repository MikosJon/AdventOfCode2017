from collections import defaultdict

instructions = []
registers = defaultdict(int)
registers['jump'] = 1

with open('input.txt') as f:
    for line in f:
        line = line.strip().split()
        instructions.append(line)

num_mul = 0
index = 0
while True:
    if index not in range(len(instructions)):
        print(num_mul)
        break

    line = instructions[index]

    op = line[0]

    if not line[1].isalpha():
        reg = 'jump'
    else:
        reg = line[1]

    if not line[2].isalpha():
        val = int(line[2])
    else:
        val = registers[line[2]]

    if op == 'set':
        registers[reg] = val
    elif op == 'sub':
        registers[reg] -= val
    elif op == 'mul':
        registers[reg] *= val
        num_mul += 1
    elif op == 'jnz' and registers[reg] != 0:
        index += val
        continue

    index += 1
