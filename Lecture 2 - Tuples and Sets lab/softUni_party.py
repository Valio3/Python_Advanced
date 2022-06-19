num_of_guests = int(input())
reservation_list = set()
for _ in range(num_of_guests):
    num = input()
    if len(num) == 8:
        reservation_list.add(num)

actual_came = set()
while True:
    command = input()

    if command == "END":
        diff = list(reservation_list.difference(actual_came))
        print(len(diff))
        [print(res_num) for res_num in sorted(diff)]
        break

    actual_came.add(command)


# def is_vip(guest):
#     return guest[0].isdigit()
#
#
# n = int(input())
#
# vip_guests = set()
# regular_guests = set()
#
# for _ in range(n):
#     reservation = input()
#     if is_vip(reservation):
#         vip_guests.add(reservation)
#     else:
#         regular_guests.add(reservation)
#
# while True:
#     guest = input()
#     if guest == 'END':
#         break
#
#     if is_vip(guest):
#         vip_guests.remove(guest)
#     else:
#         regular_guests.remove(guest)
#
# print(len(vip_guests) + len(regular_guests))
# [print(guest) for guest in sorted(vip_guests)]
# [print(guest) for guest in sorted(regular_guests)]

