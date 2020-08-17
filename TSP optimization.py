import rando
import timeit
import distance
start = timeit.default_timer()

#Read in file
file = open("test_alex.txt", "r")
num_lines = file.readline(1)
coordinates = []
for l in file:
    for line in file:
        line = line.split()
        if line:
            line = [int(i) for i in line]
            coordinates.append(line)

#Set initial point
initial_point = coordinates[0]
unvisited_points = coordinates
unvisited_points.pop(0)
order = []
order.append(initial_point)

current_point = initial_point
total_distance = 0

i = 0

while(len(unvisited_points) > 0):
    #get distances for remaining unvisited points
    j = 0
    distances = []
    for x in range(0, len(unvisited_points)):
        x1 = current_point[0]
        y1 = current_point[1]
        x2 = unvisited_points[j][0]
        y2 = unvisited_points[j][1]
        distances.append(distance.distance(x1, y1, x2, y2))
        #update current point to the closest point
        #update unvisited points list
        j += 1
    least_distance = distances[0]
    h = 0
    least_distance_point = 0
    for y in range(0, len(distances) - 1):
        if least_distance < distances[h + 1]:
            h += 1
            continue
        elif least_distance > distances[h + 1]:
            least_distance = distances[h + 1]
            least_distance_point = h + 1
        else:
            h += 1
            continue
        h += 1
    total_distance += least_distance
    order.append(unvisited_points[least_distance_point])
    current_point = unvisited_points[least_distance_point]
    unvisited_points.pop(least_distance_point)
    i += 1

last_distance = distance.distance(current_point[0], current_point[1], initial_point[0], initial_point[1])
total_distance += last_distance
current_point = initial_point
order.append(initial_point)

print (total_distance)
for z in range(0, len(order)):
    print(order[z])

stop = timeit.default_timer()

hours, rem = divmod(stop-start, 3600)
minutes, seconds = divmod(rem, 60)
print("{:0>2}:{:0>2}:{:05.2f}".format(int(hours),int(minutes),seconds))
print('Time: ', stop - start)