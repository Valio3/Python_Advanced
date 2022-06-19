def avg(values):
    return sum(values) / len(values)

students_count = int(input())
student_dict = dict()
for _ in range(students_count):
    name, grade = input().split(" ")

    if name not in student_dict.keys():
        student_dict[name] = list()
    student_dict[name].append(float(grade))

for student, grade in student_dict.items():
    print(f"{student} -> {' '.join([f'{i:.2f}' for i in grade])} (avg: {avg(grade):.2f})")
