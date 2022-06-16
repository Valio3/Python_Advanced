text = input()
stack = []
for i in text:
    stack.append(i)  # push stack

result = ""

while stack:
    result += stack.pop()
print(result)
