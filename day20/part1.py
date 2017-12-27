with open('input.txt') as f:
    particles = []
    for line in f:
        line = line.strip().split(', ')

        pos = line[0].split(',')
        vel = line[1].split(',')
        acc = line[2].split(',')

        px, py, pz = int(pos[0][3:]), int(pos[1]), int(pos[2][:-1])
        vx, vy, vz = int(vel[0][3:]), int(vel[1]), int(vel[2][:-1])
        ax, ay, az = int(acc[0][3:]), int(acc[1]), int(acc[2][:-1])

        particle = [[px, py, pz], [vx, vy, vz], [ax, ay, az]]
        particles.append(particle)

    time = 1000000
    for idx, particle in enumerate(particles):
        particle[0] = [particle[0][i] + ((particle[1][i]*time) + (particle[2][i]*time*(time+1)//2)) for i in range(3)]
        print(idx, particle[0])

    min_idx = 0    
    min_val = sum(abs(x) for x in particles[0][0])

    for i, particle in enumerate(particles):
        dist = sum(abs(x) for x in particle[0])
        if dist < min_val:
            min_val = dist
            min_idx = i

    print(min_idx)
