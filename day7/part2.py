# run file as python part2.py
import pprint
weights, children = {}, {}

with open('input.txt') as f:
    for line in f:
        line = line.strip().split(' -> ')

        first = line[0].split()
        name = first[0]
        weight = int(first[1][1:][:-1])
        weights[name] = weight 
         
        children[name] = []
        if len(line) == 2:
            for child in line[1].split(', '):
                children[name].append(child)
        else:
            children[name].append('')

def getWeight(name):
    totalWeight = weights[name]
    out = [name]
    for child in children[name]:
        if child != '':
            res = getWeight(child)
            totalWeight += res[0]
            out.append(res)
     
    return [totalWeight, out]

pprint.pprint(getWeight('ahnofa')) #find the disk, that is off weight - in my case it's ltleg (6 too much)
print(weights['ltleg'] - 6)
