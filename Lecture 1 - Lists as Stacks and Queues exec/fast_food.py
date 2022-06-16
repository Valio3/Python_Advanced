from collections import deque

food_quantity = int(input())
orders = deque([int(order) for order in input().split(" ")])
#print(max(orders))
rotates = len(orders)
current_max = 0
for i in range(rotates):
    current_order = orders.popleft()
    if current_max < current_order:
        current_max = current_order
    orders.append(current_order)
print(current_max)
result = []
while orders:
    if food_quantity - orders[0] < 0:
        [result.append(str(orders.popleft())) for _ in range(len(orders))]
        print(f"Orders left: {' '.join(result)}")
        break
    food_quantity -= orders.popleft()
if not result:
    print("Orders complete")
