# run file as python part2.py < input.txt
pos = 0
skip = 0
nums = list(range(256))

lengths = [ord(x) for x in input()] + [17, 31, 73, 47, 23]

for x in range(64):
    for length in lengths:
        temp = []
        for i in range(length):    
            temp.append(nums[(pos+i)%len(nums)])
        for j, num in enumerate(reversed(temp)):
            nums[(pos+j)%len(nums)] = num
        pos = (pos + (length + skip)) % len(nums)
        skip += 1

denseHash = []
for y in range(16):
    comb = 0
    for z in range(16):
        comb ^= nums[16*y + z]

    denseHash.append(comb)

finalHash = ''.join('{:02x}'.format(val) for val in denseHash)
print(finalHash)
