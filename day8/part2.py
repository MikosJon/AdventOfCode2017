# run file as python part2.py
from collections import defaultdict

registers = defaultdict(int)
max_value = 0

with open('input.txt') as f:
    for line in f:
        line = line.strip().split()

        reg, instruction, value, _, conditionReg, conditionOp, conditionVal = line

        if eval(f'registers["{conditionReg}"] {conditionOp} int({conditionVal})'):
            if instruction == 'inc':
                registers[reg] += int(value)
            else:
                registers[reg] -= int(value)

        max_value = max([max_value, max(registers.values())]) 

print(max_value)
