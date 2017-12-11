# run file as python part2.py < input.txt
line = input().strip().split(',')

max_dist = 0
moveN, moveNE, moveSE, moveS, moveSW, moveNW = 0,0,0,0,0,0
for step in line:
    if step == 'n':
        moveN += 1
    elif step == 'ne': 
        moveNE += 1
    elif step == 'se':
        moveSE += 1
    elif step == 's':
        moveS += 1
    elif step == 'sw':
        moveSW += 1
    elif step == 'nw':
        moveNW += 1

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

    if (moveN + moveNE + moveSE + moveS + moveSW + moveNW) > max_dist:
        max_dist = moveN + moveNE + moveSE + moveS + moveSW + moveNW
print(max_dist)
