max_len = 0
max_strength = 0

while True:
    line = input()
    if line == 'done':
        print(max_strength)
        break

    line = line.strip().split()

    new_len = int(line[0])
    new_strength = int(line[1])

    if new_len > max_len or (new_len == max_len and new_strength > max_strength):
        max_len, max_strength = new_len, new_strength

