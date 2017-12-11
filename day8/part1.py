# run file as python part1.py
from collections import defaultdict

registers = defaultdict(int)

with open('input.txt') as f:
    for line in f:
        line = line.strip().split()

        reg, instruction, value, _, conditionReg, conditionOp, conditionVal = line

        if eval(f'registers["{conditionReg}"] {conditionOp} int({conditionVal})'):
            if instruction == 'inc':
                registers[reg] += int(value)
            else:
                registers[reg] -= int(value)

print(max(registers.values()))
