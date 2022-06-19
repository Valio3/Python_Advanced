entries = int(input())

names = {input() for _ in range(entries)}

[print(name) for name in names]
