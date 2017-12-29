from collections import defaultdict
import copy

def total(pos, curr, strength, path):
    new_strength = []
    if curr not in pos:
        return strength
    for x in pos[curr]:
        new_pos = copy.deepcopy(pos)
        new_pos[curr].remove(x)
        if curr in new_pos[x]:
            new_pos[x].remove(curr)
        new_strength.append(total(new_pos, x, strength+x+curr, path+' '+str(x)))

    if new_strength:
        return max(new_strength)
    else:
        return strength


with open('input.txt') as f:
    pos = defaultdict(list)
    bridges = []
    for line in f:
        line = line.strip().split('/')

        line.sort()
        bridges.append([int(x) for x in line])

    val = set([0])
    while True:
        change = False
        to_rem = []
        for index, bridge in enumerate(bridges):
            if bridge[0] in val or bridge[1] in val:
                pos[bridge[0]].append(bridge[1])
                pos[bridge[1]].append(bridge[0])
                val.add(bridge[0])
                val.add(bridge[1])
                change = True
                to_rem.append(index)
        bridges = [bridges[i] for i in range(len(bridges)) if i not in to_rem]
        if not change:
            print(pos)
            print(total(pos, 0, 0, '0'))
            break

    
