from collections import deque

green_light = int(input())
free_window = int(input())
cars_queue = deque()
car_passed = 0
condition = True
while True:
    command = input()
    if command == "END" or green_light == 0:
        break
    if command == "green":
        current_green = green_light
        current_window = free_window
        current_car = ""
        hit_at = ""
        while cars_queue and current_green > 0:
            current_car = cars_queue.popleft()
            current_green -= len(current_car)
            if current_green > 0:
                car_passed += 1
            elif current_window + current_green >= 0:
                car_passed += 1
            else:
                diff = current_window + current_green
                hit_at = current_car[diff]
                condition = False
                break

        if not condition:
            print(f"A crash happened!")
            print(f"{current_car} was hit at {hit_at}.")
            break

    else:
        cars_queue.append(command)
if condition:
    print("Everyone is safe.")
    print(f"{car_passed} total cars passed the crossroads.")
