with open('input.txt') as f:
    patterns = {}
    for line in f:
        line = line.strip().split(' => ')

        rows = line[0].split('/')
        end = line[1].split('/')

        cols = []
        for i in range(len(rows)):
            cols.append(''.join([rows[j][i] for j in range(len(rows))]))
        
        if len(rows) == 3:
            pattern1 = '/'.join([rows[0], rows[1], rows[2]])
            pattern2 = '/'.join([cols[0][::-1], cols[1][::-1], cols[2][::-1]]) 
            pattern3 = '/'.join([rows[0][::-1], rows[1][::-1], rows[2][::-1]]) 
            pattern4 = '/'.join([cols[2], cols[1], cols[0]]) 
            pattern5 = '/'.join([rows[2][::-1], rows[1][::-1], rows[0][::-1]]) 
            pattern6 = '/'.join([cols[2][::-1], cols[1][::-1], cols[0][::-1]]) 
            pattern7 = '/'.join([rows[2], rows[1], rows[0]]) 
            pattern8 = '/'.join([cols[0], cols[1], cols[2]]) 
        else:
            pattern1 = '/'.join([rows[0], rows[1]])
            pattern2 = '/'.join([cols[0][::-1], cols[1][::-1]]) 
            pattern3 = '/'.join([rows[0][::-1], rows[1][::-1]]) 
            pattern4 = '/'.join([cols[1], cols[0]]) 
            pattern5 = '/'.join([rows[1][::-1], rows[0][::-1]]) 
            pattern6 = '/'.join([cols[1][::-1], cols[0][::-1]]) 
            pattern7 = '/'.join([rows[1], rows[0]]) 
            pattern8 = '/'.join([cols[0], cols[1]]) 
        
        all_patterns = [pattern1, pattern2, pattern3, pattern4, pattern5, pattern6, pattern7, pattern8]
        
        for pattern in all_patterns:
            patterns[pattern] = end

    state = ['.#.', '..#', '###']
    
    for iteration in range(18):
        new_state = []
        squares = []
        if len(state) % 2 == 0:
            for i in range(0, len(state), 2):
                top_rows = [state[i][pos:pos+2] for pos in range(0, len(state), 2)]
                bottom_rows = [state[i+1][pos:pos+2] for pos in range(0, len(state), 2)]
             
                squares += ['/'.join([top_rows[idx], bottom_rows[idx]]) for idx in range(len(top_rows))]
     
        else:
            for i in range(0, len(state), 3):
                top_rows = [state[i][pos:pos+3] for pos in range(0, len(state), 3)]
                middle_rows = [state[i+1][pos:pos+3] for pos in range(0, len(state), 3)]
                bottom_rows = [state[i+2][pos:pos+3] for pos in range(0, len(state), 3)]
 
                squares += ['/'.join([top_rows[idx], middle_rows[idx], bottom_rows[idx]]) for idx in range(len(top_rows))]
 
        level = 0
        for idx, square in enumerate(squares):
            new_square = patterns[square]
            if idx % int(len(squares)**0.5) == 0:
                level += 1
                for _ in range(len(new_square)):
                    new_state.append('')
            
            for index, row in enumerate(new_square): 
                new_state[len(new_square)*(level-1)+index] += row

        state = new_state
    print(str(state).count('#'))
