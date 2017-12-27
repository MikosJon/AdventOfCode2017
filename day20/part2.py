from collections import defaultdict

with open('input.txt') as f:
    particles = []
    for idx, line in enumerate(f):
        line = line.strip().split(', ')

        pos = line[0].split(',')
        vel = line[1].split(',')
        acc = line[2].split(',')

        px, py, pz = int(pos[0][3:]), int(pos[1]), int(pos[2][:-1])
        vx, vy, vz = int(vel[0][3:]), int(vel[1]), int(vel[2][:-1])
        ax, ay, az = int(acc[0][3:]), int(acc[1]), int(acc[2][:-1])

        particle = [[px, py, pz], [vx, vy, vz], [ax, ay, az], idx]
        particles.append(particle)

    for time in range(10000):
        pos = defaultdict(list)
        for idx, particle in enumerate(particles):
            particle[1][0] += particle[2][0]
            particle[1][1] += particle[2][1]
            particle[1][2] += particle[2][2]

            particle[0][0] += particle[1][0]
            particle[0][1] += particle[1][1]
            particle[0][2] += particle[1][2]

            pos[str(particle[0])].append(particle[3])
        
        to_delete = []
        for indicies in pos.values():
            if len(indicies) > 1:
                to_delete += indicies

        particles = [x for x in particles if x[3] not in to_delete]

    print(len(particles))
