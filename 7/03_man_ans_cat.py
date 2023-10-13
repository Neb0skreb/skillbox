# -*- coding: utf-8 -*-

from random import randint, choice


# Доработать практическую часть урока lesson_007/python_snippets/08_practice.py

# Необходимо создать класс кота. У кота есть аттрибуты - сытость и дом (в котором он живет).
# Кот живет с человеком в доме.
# Для кота дом характеризируется - миской для еды и грязью.
# Изначально в доме нет еды для кота и нет грязи.

# Доработать класс человека, добавив методы
#   подобрать кота - у кота появляется дом.
#   купить коту еды - кошачья еда в доме увеличивается на 50, деньги уменьшаются на 50.
#   убраться в доме - степень грязи в доме уменьшается на 100, сытость у человека уменьшается на 20.
# Увеличить кол-во зарабатываемых человеком денег до 150 (он выучил пайтон и устроился на хорошую работу :)

# Кот может есть, спать и драть обои - необходимо реализовать соответствующие методы.
# Когда кот спит - сытость уменьшается на 10
# Когда кот ест - сытость увеличивается на 20, кошачья еда в доме уменьшается на 10.
# Когда кот дерет обои - сытость уменьшается на 10, степень грязи в доме увеличивается на 5
# Если степень сытости < 0, кот умирает.
# Так же надо реализовать метод "действуй" для кота, в котором он принимает решение
# что будет делать сегодня

# Человеку и коту надо вместе прожить 365 дней.

class Man:

    def __init__(self, name, house=None):
        self.name = name
        self.house = house
        self.fullness = 50
        self.money = 100
        self.cats = []

    def __str__(self):
        return 'Я - {}, живу {}, сытость {}, денег осталось {}, {}'.format(
              self.name,
              'в доме' if self.house else 'на улице',
              self.fullness,
              self.money,
              'у меня есть котики: '+', '.join(self.cats) if self.cats else 'мечтаю завести котиков')

    def eat(self):
        if self.house.food >= 10:
            print('{} поел'.format(self.name))
            self.fullness += 20
            self.house.food -= 10
        else:
            print('{} нет еды'.format(self.name))

    def work(self):
        print('{} сходил на работу'.format(self.name))
        self.money += 150
        self.fullness -= 10

    def clean_house(self):
        print('{} почистил дом'.format(self.name))
        self.house.mud -= 100
        self.fullness -= 20

    def watch_mtv(self):
        print('{} смотрел MTV целый день'.format(self.name))
        self.fullness -= 10

    def shopping(self):

        if self.house.food <= 10 and self.money >= 50:
            self.money -= 50
            self.house.food += 50
            print('{} сходил в магазин себе за едой'.format(self.name))

        cat_food_need = len(self.cats) * 50

        if self.cats and self.house.cat_food <= len(self.cats) * 10:
            if cat_food_need <= self.money:
                self.house.cat_food += cat_food_need
                self.money -= cat_food_need
                print('{} сходил в магазин за едой кошкам'.format(self.name))
            elif cat_food_need >= self.money:
                self.house.cat_food += self.money
                self.money = 0
                print('{} сходил в магазин за едой кошкам на последние деньги'.format(self.name))

        self.fullness -= 10

    def move_in_house(self, house):
        self.house = house
        self.fullness -= 10
        print('{} Вьехал в дом'.format(self.name))

    def pick_a_cat(self, cat):
        self.cats.append(cat.name)
        self.fullness -= 5
        print('{} подобрал котика {} в дом'.format(self.name, cat.name))

    def act(self):
            if self.fullness <= 0:
                print('{} умер...'.format(self.name))
                return
            dice = randint(1, 6)
            if self.fullness < 20:
                self.eat()
            elif self.money < 100:
                self.work()
            elif self.house.food <= 10 or (self.cats and self.house.cat_food <= len(self.cats) * 10):
                self.shopping()
            elif self.fullness > 20 and self.house.mud >= 100:
                self.clean_house()
            elif dice == 1:
                self.watch_mtv()
            elif dice == 2:
                self.eat()
            else:
                self.work()


class House:

    def __init__(self):
        self.food = 50
        self.mud = 20
        self.cat_food = 0

    def __str__(self):
        return 'В доме еды осталось {}, кошачьей еды {}, грязи {}'.format(self.food,
                                                                          self.cat_food,
                                                                          self.mud)


class Cat:

    def __init__(self, name, house=None):
        self.name = name
        self.fullness = randint(1, 6) * 10
        self.house = house

    def __str__(self):
        return 'Я {} котик - {}, сытость {}'.format('домашний' if self.house else 'уличный',self.name, self.fullness)

    def eat(self):

        if self.house:
            if self.house.cat_food > 0:
                self.fullness += 20
                self.house.cat_food -= 10
                print('{} котик {} покушал, сытость {}'.format('Домашний' if self.house else 'уличный',
                                                                self.name,
                                                                self.fullness))
        else:
            dice = randint(1, 6)
            if dice == 1:
                self.fullness -= 10
                print('Уличный котик {} НЕ поймал мышь, сытость {}'.format(self.name, self.fullness))
            else:
                self.fullness += 20
                print('Уличный котик {} поймал мышь, сытость {}'.format(self.name, self.fullness))

    def play(self):
        self.fullness -= 10
        self.house.mud += 5
        print('{} котик {} поиграл, сытость {}'.format('Домашний' if self.house else 'уличный',
                                                        self.name,
                                                        self.fullness))

    def sleep(self):
        if self.house:
            self.fullness -= 10
            self.house.mud += 5
            print('{} котик {} поспал, сытость {}'.format('Домашний' if self.house else 'уличный',
                                                           self.name,
                                                           self.fullness))
        else:
            self.fullness -= 10
            print('Уличный котик {} спит, сытость {}'.format(self.name, self.fullness))

    def tear_wallpaper(self):
        self.fullness -= 10
        self.house.mud += 5
        print('{} котик {} драл обои, сытость {}'.format('Домашний' if self.house else 'уличный',
                                                          self.name,
                                                          self.fullness))

    def settle_in_house(self, house):
        self.house = house
        print('Котик {} переехал в дом'.format(self.name, self.fullness))

    def feces(self):
        self.house.mud += 20
        self.fullness -= 10
        print('{} котик {} нагадил, сытость {}'.format('Домашний' if self.house else 'уличный',
                                                        self.name,
                                                        self.fullness))

    def act(self):
        dice = randint(1, 6)
        if self.fullness < 0:
            print('Котик {} сдох'.format(self.name))
        elif self.fullness <= 10:
            self.eat()
        elif self.house and dice == 1:
            self.play()
        elif self.house and dice == 2:
            self.feces()
        elif self.house and dice == 3:
            self.tear_wallpaper()
        else:
            self.sleep()


sweet_home = House()
print(sweet_home)

man = Man(name='Кузьма', house=sweet_home)
print(man)

street_cats = [
    Cat('Барсик'),
    Cat('Рыжик'),
    Cat('Пончик'),
    Cat('Матильда'),
]

home_cats = [Cat(name='Хрящик', house=sweet_home),]

for cat in street_cats:
    print(cat)

for cat in home_cats:
    print(cat)

for day in map(str, range(1, 366)):
    print('=== день '+day+' ===')

    if man.house:
        if day == 1 and home_cats:
            for cat in home_cats:
                man.cats.append(cat.name)

        man.act()
        print(man)

        if man.money // (len(man.cats) + 1) >= 200:
            if len(street_cats) > 0:
                some_cat = choice(street_cats)
                home_cats.append(some_cat)
                man.pick_a_cat(some_cat)
                some_cat.settle_in_house(sweet_home)
                street_cats.remove(some_cat)
    else:
        man.move_in_house(sweet_home)
        '''приручаем котиков живущих в доме'''
        if home_cats:
            for cat in home_cats:
                man.cats.append(cat.name)

    print(sweet_home)

    for cat in street_cats:
        cat.act()

    for cat in home_cats:
        cat.act()

print('**********************')
print('Итоги года:')

for cat in home_cats:
    print(cat)

for cat in street_cats:
    print(cat)

print(man)
print('**********************')
