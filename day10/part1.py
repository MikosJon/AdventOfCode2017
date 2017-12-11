# run file as python part1.py < input.txt
pos = 0
skip = 0
nums = list(range(256))

lengths = [int(x) for x in input().strip().split(',')]

for length in lengths:
    temp = []
    for i in range(length):    
        temp.append(nums[(pos+i)%len(nums)])
    for j, num in enumerate(reversed(temp)):
        nums[(pos+j)%len(nums)] = num
    pos = (pos + (length + skip)) % len(nums)
    skip += 1

print(nums[0] * nums[1])
