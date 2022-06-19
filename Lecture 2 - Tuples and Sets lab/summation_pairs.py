unique_nums = [int(num) for num in input().split()]
target = int(input())
iter = 0
result_set = set()
for iteration in range(len(unique_nums)):
    for iteration2 in range(iteration + 1, len(unique_nums)):
        iter += 1
        if unique_nums[iteration] + unique_nums[iteration2] == target:
            result_set.add(f"({unique_nums[iteration]}, {unique_nums[iteration2]})")
            print(f"{unique_nums[iteration]} + {unique_nums[iteration2]} = {target}")

print(f"Iterations done: {iter}")
[print(pair) for pair in result_set]
