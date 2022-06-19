from collections import deque

bullet_price = int(input())
barrel_size = int(input())
bullets_stack = [int(i) for i in input().split()]
locks = deque([int(i) for i in input().split()])
intelligence_value = int(input())
bullets_count = 0
current_barrel = barrel_size

while bullets_stack and locks:
    shoot_bullet = bullets_stack.pop()
    bullets_count += 1
    if shoot_bullet <= locks[0]:
        print("Bang!")
        locks.popleft()
    else:
        print("Ping!")

    current_barrel -= 1
    if current_barrel == 0 and bullets_stack:
        print("Reloading!")
        current_barrel = barrel_size

if locks:
    print(f"Couldn't get through. Locks left: {len(locks)}")
else:
    print(f"{len(bullets_stack)} bullets left. Earned ${intelligence_value - (bullets_count * bullet_price)}")

