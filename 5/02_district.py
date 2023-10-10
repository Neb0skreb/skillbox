# -*- coding: utf-8 -*-

# Составить список всех живущих на районе и Вывести на консоль через запятую
# Формат вывода: На районе живут ...
# подсказка: для вывода элементов списка через запятую можно использовать функцию строки .join()
# https://docs.python.org/3/library/stdtypes.html#str.join

import district.central_street.house1.room1 as central_street_house_1_room_1
import district.central_street.house1.room2 as central_street_house_1_room_2
import district.central_street.house2.room1 as central_street_house_2_room_1
import district.central_street.house2.room2 as central_street_house_2_room_2
import district.soviet_street.house1.room1 as soviet_street_house_1_room_1
import district.soviet_street.house1.room2 as soviet_street_house_1_room_2
import district.soviet_street.house2.room1 as soviet_street_house_2_room_1
import district.soviet_street.house2.room2 as soviet_street_house_2_room_2

rooms = [
    central_street_house_1_room_1, central_street_house_1_room_2,
    central_street_house_2_room_1, central_street_house_2_room_2,
    soviet_street_house_1_room_1, soviet_street_house_1_room_2,
    soviet_street_house_2_room_1, soviet_street_house_2_room_2
]

total_people_in_street = []

for room in rooms:
    if room.folks:
        total_people_in_street.extend(room.folks)

if total_people_in_street:
    total_people_in_street_str = ", ".join(total_people_in_street) + "."
    print(total_people_in_street_str)




