from collections import defaultdict

with open('input.txt') as f:
    instructions = []
    sounds = []
    registers = defaultdict(int)
    index = 0

    for line in f:
        line = line.strip().split()
        instructions.append(line)

    while True:
        if index not in range(len(inctructions)):
            break

        line = instructions[index]
        op = line[0]
        reg = line[1]
        
        if op == 'rcv' and registers[reg]:
            print(sounds[-1])
            break
        elif op == 'snd':
            sounds.append(registers[reg])
        else:
            if line[2] in 'abcdefghijklmnopqrstuvwxzy':
                val = registers[line[2]]
            else:
                val = int(line[2])
            
            if op == 'set':
                registers[reg] = val
            elif op == 'add':
                registers[reg] += val
            elif op == 'mul':
                registers[reg] *= val
            elif op == 'mod':
                registers[reg] %= val
            elif op == 'jgz' and registers[reg] > 0:
                index += val
                continue
        
        index += 1
