# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1200, 800)
snowflake_size = {'min': 5, 'max': 20}

_snowflakes = {}
_down_snowflakes = []


def create_snowflakes(snowflakes_count=1):
    new_snowflakes = {}

    for i in range(snowflakes_count):
        new_snowflakes[len(_snowflakes) + i] = {
            'length': sd.random_number(snowflake_size['min'], snowflake_size['max']),
            'x': sd.random_number(0, sd.resolution[0]),
            'y': 700,
            'factor_a': sd.random_number(1, 10) / 10,
            'factor_b': sd.random_number(1, 10) / 10,
            'factor_c': sd.random_number(1, 120)
        }

    _snowflakes.update(new_snowflakes)
    _down_snowflakes.clear()


def remove_snowflakes(num_snowflake):
    for num in num_snowflake:
        _snowflakes.pop(num, None)


def draw_snowflakes(color=sd.COLOR_WHITE):
    for snowflake_num, snowflake_parameter in _snowflakes.items():
        start_point = sd.get_point(x=snowflake_parameter['x'], y=snowflake_parameter['y'])
        sd.snowflake(center=start_point,
                     length=snowflake_parameter['length'],
                     color=color,
                     factor_a=snowflake_parameter['factor_a'],
                     factor_b=snowflake_parameter['factor_b'],
                     factor_c=snowflake_parameter['factor_c'])


def move_snowflakes():
    for snowflake_num, snowflake_parameter in _snowflakes.items():
        snowflake_parameter['x'] += sd.random_number(0, 2)
        snowflake_parameter['y'] -= snowflake_size['max'] + 1 - snowflake_parameter['length']


def get_down_snowflakes():
    down_snowflakes = [snowflake_num for snowflake_num, snowflake_parameter in _snowflakes.items() if snowflake_parameter['y'] < 0]
    return down_snowflakes
