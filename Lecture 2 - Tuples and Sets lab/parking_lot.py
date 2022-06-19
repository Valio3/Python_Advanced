num_commands = int(input())
car_lot = set()
# parking_logs = [input().split(", ") for _ in range(num_commands)]
# for direction, car_number in parking_logs:

for _ in range(num_commands):
    way, car_number = input().split(", ")
    if way == "IN":
        car_lot.add(car_number)
    elif way == "OUT":
        car_lot.remove(car_number)
if not car_lot:
    print("Parking Lot is Empty")
else:
    [print(car) for car in car_lot]
