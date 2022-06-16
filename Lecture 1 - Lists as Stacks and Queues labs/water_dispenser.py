from collections import deque

water_quantity = int(input())
people_queue = deque()
while True:
    people = input()
    if people == "Start":
        break

    people_queue.append(people)

while True:

    command = input()
    if command == "End":
        print(f"{water_quantity} liters left")
        break

    if "refill" in command:  # or startswith("refill")
        liters = command.split()[1]
        water_quantity += int(liters)
    else:
        liters = int(command)
        if water_quantity - liters >= 0:
            water_quantity -= liters
            print(f"{people_queue.popleft()} got water")
        else:
            print(f"{people_queue.popleft()} must wait")
