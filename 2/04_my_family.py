#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Создайте списки:

# моя семья (минимум 3 элемента)
my_family = ['pavel','evgeniya','eva']


# список списков приблизителного роста членов вашей семьи
my_family_height = [
    # ['имя', рост],
    [my_family[0], 192],
    [my_family[1], 165],
    [my_family[2], 99]
]

# Выведите на консоль отца в формате
#   Рост Zoizehn - ХХ см
print(f'Рост {my_family[0]} {my_family_height[0][1]} см')
# Выведите на консоль общий рост вашей семьи как сумму ростов всех членов
#   Общий рост моей семьи - ХХ см
height_sum = 0

for i in my_family_height:
    height_sum += i[1]

print(height_sum)