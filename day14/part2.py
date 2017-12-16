from collections import deque

def getHash(string):
    pos = 0
    skip = 0
    nums = list(range(256))

    lengths = [ord(x) for x in string] + [17, 31, 73, 47, 23]
    
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
    return finalHash

def connected(row, col):
    out = set()
    movements = [
        (-1, 0),
        (0, -1),
        (0, 1),
        (1, 0),
    ]

    for drow, dcol in movements: 
        if grid[min([max([row+drow, 0]), 127])][min([max([col+dcol, 0]), 127])]:
            out.add((min([max([row+drow, 0]), 127]), min([max([col+dcol, 0]), 127])))

    return out

start = input().strip()
grid = [[int(bit) for bit in '{:0128b}'.format(int(getHash('{}-{}'.format(start, i)), 16))] for i in range(128)]

 
numGroups = 0
visited = []
for i in range(128):
    for j in range(128):
        if 128*i + j not in visited and grid[i][j]:
            numGroups += 1
            queue = deque(connected(i,j))
            while queue:
                curr = queue.pop()
                if 128*curr[0] + curr[1] not in visited:
                    visited.append(128*curr[0] + curr[1])
                    queue.extend(connected(*curr))

print(numGroups)
