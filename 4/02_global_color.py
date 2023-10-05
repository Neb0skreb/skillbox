# -*- coding: utf-8 -*-
import simple_draw as sd

# Добавить цвет в функции рисования геом. фигур. из упр lesson_004/01_shapes.py
# (код функций скопировать сюда и изменить)
# Запросить у пользователя цвет фигуры посредством выбора из существующих:
#   вывести список всех цветов с номерами и ждать ввода номера желаемого цвета.
# Потом нарисовать все фигуры этим цветом

# Пригодятся функции
# sd.get_point()
# sd.line()
# sd.get_vector()
# и константы COLOR_RED, COLOR_ORANGE, COLOR_YELLOW, COLOR_GREEN, COLOR_CYAN, COLOR_BLUE, COLOR_PURPLE
# Результат решения см lesson_004/results/exercise_02_global_color.jpg

def get_color(number):
    colors = {
        0: sd.COLOR_RED,
        1: sd.COLOR_ORANGE,
        2: sd.COLOR_YELLOW,
        3: sd.COLOR_GREEN,
        4: sd.COLOR_CYAN,
        5: sd.COLOR_BLUE,
        6: sd.COLOR_PURPLE,
    }
    return colors.get(number, sd.COLOR_YELLOW)  # Возвращаем желтый цвет по умолчанию

def input_color():
    print("Possible colors:")
    print("0: red")
    print("1: orange")
    print("2: yellow")
    print("3: green")
    print("4: cyan")
    print("5: blue")
    print("6: purple")

    while True:
        try:
            user_input = int(input("Enter a number for shapes color > "))
            if 0 <= user_input <= 6:
                return user_input
            else:
                print("Invalid input, must be a number between 0 - 6")
        except ValueError:
            print("Invalid input, must be a number")

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

point1 = sd.get_point(50, 50)
point2 = sd.get_point(380, 50)
point3 = sd.get_point(150, 380)
point4 = sd.get_point(450, 380)
point5 = sd.get_point(200, 200)

user_color = input_color()
color_tuple = get_color(number=user_color)

draw_shape(point_bottom_left=point1, lines_count=3, angle=30, length=110, width=5, color=color_tuple)
draw_shape(point_bottom_left=point2, lines_count=4, angle=20, length=110, width=5, color=color_tuple)
draw_shape(point_bottom_left=point3, lines_count=5, angle=60, length=110, width=5, color=color_tuple)
draw_shape(point_bottom_left=point4, lines_count=6, angle=35, length=110, width=5, color=color_tuple)

sd.pause()