text = input()
stack = []

for index in range(len(text)):
    if text[index] == "(":
        stack.append(index)
    elif text[index] == ")":
        start_exp = (stack.pop())
        print(text[start_exp:index + 1])
