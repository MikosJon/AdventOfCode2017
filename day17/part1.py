steps = int(input().strip())

pos = 0
buff = [0] 

for val in range(1, 2018):
    pos = (pos + steps + 1) % len(buff)
    buff.insert(pos, val)

print(buff[(pos+1)%len(buff)])
