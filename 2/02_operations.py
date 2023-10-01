# # -*- coding: utf-8 -*-
#
# # Расставьте знаки операций "плюс", "минус", "умножение" и скобки
# # между числами "1 2 3 4 5" так, что бы получилось число "25".
# #
# # Использовать нужно только указанные знаки операций, но не обязательно все перечесленные.
# # Порядок чисел нужно сохранить.
#

#
# # TODO написать формулу для 1 2 3 4 5 и вывести значение на консоль
def find_expression(numbers, target, current_expression="", current_result=0, current_index=0):
    if current_index == len(numbers):
        if current_result == target:
            print(current_expression)
        return

    find_expression(numbers, target, current_expression + "+" + str(numbers[current_index]),
                    current_result + numbers[current_index], current_index + 1)

    find_expression(numbers, target, current_expression + "-" + str(numbers[current_index]),
                    current_result - numbers[current_index], current_index + 1)

    find_expression(numbers, target, current_expression + "*" + str(numbers[current_index]),
                    current_result * numbers[current_index], current_index + 1)


numbers = [1, 2, 3, 4, 5]
target = 25
find_expression(numbers, target)
