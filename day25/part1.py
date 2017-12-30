from collections import defaultdict

pos = 0
tape = defaultdict(int)

state = 'A'
num_steps = 12386363

for _ in range(num_steps):
    if state == 'A':
        if tape[pos] == 0:
            tape[pos] = 1
            pos += 1
            state = 'B'
        elif tape[pos] == 1:
            tape[pos] = 0
            pos -= 1
            state = 'E'

    elif state == 'B':
        if tape[pos] == 0:
            tape[pos] = 1
            pos -= 1
            state = 'C'
        elif tape[pos] == 1:
            tape[pos] = 0
            pos += 1
            state = 'A'

    elif state == 'C':
        if tape[pos] == 0:
            tape[pos] = 1
            pos -= 1
            state = 'D'
        elif tape[pos] == 1:
            tape[pos] = 0
            pos += 1
            state = 'C'
        
    elif state == 'D':
        if tape[pos] == 0:
            tape[pos] = 1
            pos -= 1
            state = 'E'
        elif tape[pos] == 1:
            tape[pos] = 0
            pos -= 1
            state = 'F'
        
    elif state == 'E':
        if tape[pos] == 0:
            tape[pos] = 1
            pos -= 1
            state = 'A'
        elif tape[pos] == 1:
            tape[pos] = 1
            pos -= 1
            state = 'C'

    elif state == 'F':
        if tape[pos] == 0:
            tape[pos] = 1
            pos -= 1
            state = 'E'
        elif tape[pos] == 1:
            tape[pos] = 1
            pos += 1
            state = 'A'

print(sum(tape.values()))

