# run file as python part1.py < input.txt
line = input().strip().split(',')

moveN = line.count('n')
moveS = line.count('s')
moveSE = line.count('se')
moveSW = line.count('sw')
moveNE = line.count('ne')
moveNW = line.count('nw')

end = False
while not end:
    end = True
    if moveSE and moveSW:
        moveSE -= 1
        moveSW -=1
        moveS += 1
        end = False
    elif moveNE and moveNW:
        moveNE -= 1
        moveNW -= 1
        moveN += 1
        end = False
    elif moveNE and moveS:
        moveNE -= 1
        moveS -= 1
        moveSE += 1
        end = False
    elif moveNW and moveS:
        moveNW -= 1
        moveS -= 1
        moveSW += 1
        end = False
    elif moveSW and moveN:
        moveSW -= 1
        moveN -= 1
        moveNW += 1
        end = False
    elif moveSE and moveN:
        moveSE -= 1
        moveN -= 1
        moveNE += 1
        end = False
    elif moveS and moveN:
        moveS -= 1
        moveN -= 1
        end = False
    elif moveSE and moveNW:
        moveSE -= 1
        moveNW -= 1
        end = False
    elif moveSW and moveNE: 
        moveSW -= 1
        moveNE -= 1
        end = False

print(moveN + moveNE + moveSE + moveS + moveSW + moveNW)
