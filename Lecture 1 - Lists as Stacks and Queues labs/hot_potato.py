from collections import deque

kids = input()
tosses = int(input())
kids_queue = deque(kids.split())

current_toss = 0

while len(kids_queue) > 1:
    current_toss += 1
    current_kid = kids_queue.popleft()

    if current_toss < tosses:
        kids_queue.append(current_kid)
    else:
        print(f"Removed {current_kid}")
        current_toss = 0
print(f"Last is {kids_queue.popleft()}")


