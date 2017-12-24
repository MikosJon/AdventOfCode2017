with open('input.txt') as f:
    grid = []
    for line in f:
        line = line[:-1][1:]
        grid.append(line)

    letters = '' 
    x, y = 0, 0
    direction = 'S'

    while True:
        if direction == 'S':     
            while grid[x][y] != '+':
                x += 1
                if grid[x][y].isalpha():
                    print(x,y)
                    letters += grid[x][y]
                if grid[x][y] == ' ':
                    break

            pos1 = max([0, y-1])
            pos2 = min([len(grid[x]), y+1])
            
            if grid[x][pos1] == '-':
                direction = 'W'
                y = pos1
            elif grid[x][pos2] == '-':
                direction = 'E'
                y = pos2
            else:
                print(letters)
                break

        elif direction == 'N':     
            while grid[x][y] != '+':
                x -= 1
                if grid[x][y].isalpha():
                    print(x,y)
                    letters += grid[x][y]
                if grid[x][y] == ' ':
                    break

            pos1 = max([0, y-1])
            pos2 = min([len(grid[x]), y+1])
            
            if grid[x][pos1] == '-':
                direction = 'W'
                y = pos1
            elif grid[x][pos2] == '-':
                direction = 'E'
                y = pos2
            else:
                print(letters)
                break

        elif direction == 'E':     
            while grid[x][y] != '+':
                y += 1
                if grid[x][y].isalpha():
                    print(x,y)
                    letters += grid[x][y]
                if grid[x][y] == ' ':
                    break
                    
            pos1 = max([0, x-1])
            pos2 = min([len(grid), x+1])
            
            if grid[pos1][y] == '|':
                direction = 'N'
                x = pos1
            elif grid[pos2][y] == '|':
                direction = 'S'
                x = pos2
            else:
                print(letters)
                break

        elif direction == 'W':     
            while grid[x][y] != '+':
                y -= 1
                if grid[x][y].isalpha():
                    print(x,y)
                    letters += grid[x][y]
                if grid[x][y] == ' ':
                    break

            pos1 = max([0, x-1])
            pos2 = min([len(grid), x+1])
            
            if grid[pos1][y] == '|':
                direction = 'N'
                x = pos1
            elif grid[pos2][y] == '|':
                direction = 'S'
                x = pos2
            else:
                print(letters)
                break
