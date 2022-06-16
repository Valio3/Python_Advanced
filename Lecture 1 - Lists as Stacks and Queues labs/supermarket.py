from collections import deque

queue = deque()
while True:
    text = input()
    if text == "End":
        print(f"{len(queue)} people remaining.")
        break
    else:
        if text != "Paid":
            queue.append(text)
            continue
        while queue:
            print(queue.popleft())
