numbers = [float(i) for i in input().split()]
dict_occurrence = dict()

for i in numbers:

    if i not in dict_occurrence.keys():
        dict_occurrence[i] = 0
    dict_occurrence[i] += 1

for num, occur in dict_occurrence.items():
    print(f"{num:.1f} - {occur} times")

