from collections import defaultdict

with open('input.txt') as f:
    instructions = []
    registers0, registers1 = defaultdict(int), defaultdict(int)
    registers0['p'] = 0
    registers1['p'] = 1
    index0, index1 = 0, 0
    prog0, prog1 = True, True
    queue = [[],[]]
    count = 0

    for line in f:
        line = line.strip().split()
        instructions.append(line)

    while True:
        if index0 not in range(len(instructions)):
            prog0 = False
            print('prog0 out of range')
            break
        if index1 not in range(len(instructions)):
            prog1 = False
            print('prog1 out of range')
            break
        
        if not prog0 and not prog1:
            print(count)
            break

        line0 = instructions[index0]
        line1 = instructions[index1]

        op0 = line0[0]
        op1 = line1[0]

        reg0 = line0[1]
        reg1 = line1[1]
        
        if op0 == 'rcv':
            if len(queue[0]) > 0:
                registers0[reg0] = queue[0].pop(0)
                prog0 = True
            else:
                index0 -= 1
                prog0 = False
        elif prog0:
            if op0 == 'snd':
                queue[1].append(registers0[reg0])
            else:
                if line0[2] in 'abcdefghijklmnopqrstuvwxyz':
                    val0 = registers0[line0[2]]
                else:
                    val0 = int(line0[2])
             
                if op0 == 'set':
                    registers0[reg0] = val0
                elif op0 == 'add':
                    registers0[reg0] += val0
                elif op0 == 'mul':
                    registers0[reg0] *= val0
                elif op0 == 'mod':
                    registers0[reg0] %= val0
                elif op0 == 'jgz':
                    if reg0 in 'abcdefghijklmnopqrstuvwxyz':
                        if registers0[reg0] > 0:
                            index0 += (val0-1)
                    elif int(reg0) > 0:
                        index0 += (val0-1)

        if op1 == 'rcv':
            if len(queue[1]) > 0:
                registers1[reg1] = queue[1].pop(0)
                prog1 = True
            else:
                prog1 = False
                index1 -= 1
        elif prog1:
            if op1 == 'snd':
                queue[0].append(registers1[reg1])
                count += 1
            else:
                if line1[2] in 'abcdefghijklmnopqrstuvwxzy':
                    val1 = registers1[line1[2]]
                else:
                    val1 = int(line1[2])
             
                if op1 == 'set':
                    registers1[reg1] = val1
                elif op1 == 'add':
                    registers1[reg1] += val1
                elif op1 == 'mul':
                    registers1[reg1] *= val1
                elif op1 == 'mod':
                    registers1[reg1] %= val1
                elif op1 == 'jgz':
                    if reg1 in 'abcdefghijklmnopqrstuvwxyz':
                        if registers1[reg1] > 0:
                            index1 += (val1-1)
                    elif int(reg1) > 0:
                        index1 += (val1-1)
        
        index0 += 1
        index1 += 1
        print(line0, registers0)
        print(line1, registers1)
        print(count)
        print()
