# run file as python part1.py < input.txt
stream = input()

score = 0
level = 0
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
    pos += 1

print(score)
