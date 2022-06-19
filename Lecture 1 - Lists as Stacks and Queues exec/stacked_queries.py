queries = int(input())
stack = list()
for _ in range(queries):
    command = input()

    if len(command.split()) > 1:
        number = int(command.split()[1])
        stack.append(number)

    else:
        if command == "2" and len(stack) > 0:
            stack.pop()

        elif command == "3" and len(stack) > 0:
            print(max(stack))

        elif command == "4" and len(stack) > 0:
            print(min(stack))
result_stack = []
while len(stack) > 0:
    result_stack.append(str(stack.pop()))
print(", ".join(result_stack))
