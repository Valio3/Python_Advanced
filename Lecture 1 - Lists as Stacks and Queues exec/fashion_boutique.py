clothes_in_box = [int(i) for i in input().split()]
rack_capacity = int(input())
racks_num = 0
current_rack_sum = 0
if clothes_in_box:
    racks_num = 1
while clothes_in_box:
    if current_rack_sum == rack_capacity or current_rack_sum + clothes_in_box[-1] > rack_capacity:
        racks_num += 1
        current_rack_sum = 0
    current_rack_sum += clothes_in_box.pop()

print(racks_num)

# clothes_in_box = [int(i) for i in input().split()]
# rack_capacity = int(input())
# racks_num = 0
# current_rack_sum = 0
# if clothes_in_box:
#     racks_num = 1
# while clothes_in_box:
#     if current_rack_sum == rack_capacity:
#         racks_num += 1
#         current_rack_sum = 0
#     elif current_rack_sum + clothes_in_box[-1] > rack_capacity:
#         racks_num += 1
#         current_rack_sum = 0
#     current_rack_sum += clothes_in_box.pop()
#
# print(racks_num)