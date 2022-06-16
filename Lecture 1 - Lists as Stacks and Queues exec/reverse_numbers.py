nums = input().split(" ")
stack = list()

for digit in nums:
    stack.append(digit)
while len(stack) > 0:
    print(stack.pop(), end=' ')

