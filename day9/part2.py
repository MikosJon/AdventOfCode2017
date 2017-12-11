# run file as python part2.py < input.txt
stream = input()

score = 0
level = 0
pieces = 0
garbage = False

pos = 0
while pos < len(stream):
    char = stream[pos]
    if not garbage:
        if char == '{':
            level += 1
        elif char == '}':
            score += level
            level -= 1
        elif char == '<':
            garbage = True
    else:
        if char == '!':
            pos += 2
            continue
        elif char == '>':
            garbage = False
        else:
            pieces += 1
    pos += 1

print(pieces)
