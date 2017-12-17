factorA = 16807
factorB = 48271
divider = 2147483647
count = 0

def generatorA():
    genA = int(input().strip().split()[-1])
    while True:
        genA = genA * factorA % divider
        if genA % 4 == 0:
            yield genA

def generatorB():
    genB = int(input().strip().split()[-1])
    while True:
        genB = genB * factorB % divider
        if genB % 8 == 0:
            yield genB

valA = generatorA()
valB = generatorB()

for asdf in range(5000000):
    binA = '{:016b}'.format(next(valA))
    binB = '{:016b}'.format(next(valB))

    if binA[-16:] == binB[-16:]:
        count += 1

print(count)
