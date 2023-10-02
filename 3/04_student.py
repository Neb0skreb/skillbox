# -*- coding: utf-8 -*-

# (цикл while)

# Ежемесячная стипендия студента составляет educational_grant руб., а расходы на проживание превышают стипендию
# и составляют expenses руб. в месяц. Рост цен ежемесячно увеличивает расходы на 3%, кроме первого месяца
# Составьте программу расчета суммы денег, которую необходимо единовременно попросить у родителей,
# чтобы можно было прожить учебный год (10 месяцев), используя только эти деньги и стипендию.
# Формат вывода:
#   Студенту надо попросить ХХХ.ХХ рублей

educational_grant, expenses = 10000, 12000

i = 10

money_to_ask_from_parents = educational_grant * i

while i > 0:
    money_to_ask_from_parents -= expenses
    expenses *= 1.03
    i -= 1

money_to_ask_from_parents *= -1
money_to_ask_from_parents = round(money_to_ask_from_parents, 2)
print("Студенту надо попросить", money_to_ask_from_parents, "рублей")
