# run file as python part2.py
with open('input.txt') as f:
    count = 0
    for line in f:
        print('start line')
        flag = False
        line = line.split()
        for num in line:
            for num2 in line:
                if int(num) % int(num2) == 0 and num != num2:
                    count += int(num) / int(num2)
                    flag = True
                    break
            if flag:
                break

    print(count)
