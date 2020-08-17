import rando
import timeit
import numpy as np
import distance
start = timeit.default_timer()

#Read in file
file = open("test1.txt", "r")
num_lines = file.readline(1)
coordinates = []
for l in file:
    for line in file:
        line = line.split()
        if line:
            line = [int(i) for i in line]
            coordinates.append(line)
size = len(coordinates)
coor = np.array(coordinates)
print(coordinates)
print(coor)

from itertools import permutations
coor_permutations = list(permutations(coor))

b = 0
least_distance_path = 0
min_distance = 10000000000
for a in range(0, len(coor_permutations)):
    dist = 0
    d = 1
    for c in range(size - 1):
        x1 = coor_permutations[a][c][0]
        y1 = coor_permutations[a][c][1]
        x2 = coor_permutations[a][c+1][0]
        y2 = coor_permutations[a][c+1][1]
        dist += distance.distance(x1, y1, x2, y2)
        if d == size - 1:
            x1 = coor_permutations[a][c+1][0]
            y1 = coor_permutations[a][c+1][1]
            x2 = coor_permutations[a][0][0]
            y2 = coor_permutations[a][0][1]
            dist += distance.distance(x1, y1, x2, y2)
        d += 1
    if dist < min_distance:
        min_distance = dist
        least_distance_path = b
    b += 1

print(min_distance)
for z in range(0, len(coor_permutations[least_distance_path])):
    print(coor_permutations[least_distance_path][z])
print(coor_permutations[least_distance_path][0])

stop = timeit.default_timer()

hours, rem = divmod(stop-start, 3600)
minutes, seconds = divmod(rem, 60)
print("{:0>2}:{:0>2}:{:05.2f}".format(int(hours),int(minutes),seconds))

print('Time: ', stop - start)