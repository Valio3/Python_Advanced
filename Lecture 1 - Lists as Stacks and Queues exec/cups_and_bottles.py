from collections import deque

cup_capacity = deque([int(i) for i in input().split()])
bottle_capacity_stack = [int(i) for i in input().split()]
wasted_water = 0
while cup_capacity and bottle_capacity_stack:
    current_bottle = bottle_capacity_stack.pop()
    current_cup = cup_capacity.popleft()
    while current_cup > current_bottle:
        current_cup -= current_bottle
        current_bottle = bottle_capacity_stack.pop()
        continue
    wasted_water += current_bottle - current_cup

if cup_capacity:
    #     result = list()
    #     while cup_capacity:
    #         result.append(str(cup_capacity.popleft()))
    print(f"Cups: {' '.join([str(i) for i in cup_capacity])}\n"
          f"Wasted litters of water: {wasted_water}")
else:
    # Do like it is stack

    print(f"Bottles: {' '.join([str(i) for i in bottle_capacity_stack])}\n"
          f"Wasted litters of water: {wasted_water}")
