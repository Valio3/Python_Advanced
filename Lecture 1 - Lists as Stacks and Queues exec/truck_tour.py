from collections import deque
pumps = deque()
petrol_pumps_count = int(input())
for _ in range(petrol_pumps_count):
    pumps.append([int(i) for i in input().split()])


for initial_point in range(petrol_pumps_count):
    truck_petrol = 0
    condition = False
    for petrol, distance in pumps:
        truck_petrol += petrol - distance
        if truck_petrol < 0:
            condition = True
            break
    if condition:
        pumps.append(pumps.popleft())
    else:
        print(initial_point)
        break
