# -*- coding: utf-8 -*-

import simple_draw as sd

# Запросить у пользователя желаемую фигуру посредством выбора из существующих
#   вывести список всех фигур с номерами и ждать ввода номера желаемой фигуры.
# и нарисовать эту фигуру в центре экрана

# Код функций из упр lesson_004/02_global_color.py скопировать сюда
# Результат решения см lesson_004/results/exercise_03_shape_select.jpg

def draw_shape(point_bottom_left, lines_count=3, angle=0, length=100, width=3, color=sd.COLOR_YELLOW):
    figure_angle = (360 / lines_count)
    v1 = None

    for i in range(lines_count):
        if v1:
            if i == lines_count - 1:
                sd.line(start_point=v1.end_point, end_point=point_bottom_left, width=width, color=color)
            else:
                v1 = sd.get_vector(start_point=v1.end_point, angle=angle + i * figure_angle, length=length, width=width)
            v1.draw(color=color)
        else:
            v1 = sd.get_vector(start_point=point_bottom_left, angle=angle, length=length, width=width)
            v1.draw(color=color)

def draw_figure(point_middle, figure_type, length=100, color=sd.COLOR_YELLOW):
    figures = {
        0: lambda: draw_shape(point_bottom_left=point_middle, lines_count=3, length=length, width=5, color=color),
        1: lambda: draw_shape(point_bottom_left=point_middle, lines_count=4, length=length, width=5, color=color),
        2: lambda: draw_shape(point_bottom_left=point_middle, lines_count=5, length=length, width=5, color=color),
        3: lambda: draw_shape(point_bottom_left=point_middle, lines_count=6, length=length, width=5, color=color),
    }
    draw_function = figures.get(figure_type)
    if draw_function:
        draw_function()

print("Possible shapes:")
print("0: triangle")
print("1: square")
print("2: pentagon")
print("3: hexagon")

while True:
    try:
        user_input = int(input("Enter a number for a shape > "))
        if 0 <= user_input <= 3:
            break
        else:
            print("Invalid input, must be a number between 0 - 3")
    except ValueError:
        print("Invalid input, must be a number")

point_middle = sd.get_point(250, 250)
draw_figure(point_middle, user_input, length=110)

sd.pause()
