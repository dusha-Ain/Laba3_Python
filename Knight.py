import random as rd

CONST_N = 30
CONST_M = 2


class Knight(object):

    """объект типа рыцарь"""

    # описание основных параметров класса рыцарь
    __health = 0
    __damage = 0
    __color_of_the_banner = ''

    def __init__(self, hp=None, dm=None, color=None):
        self.__health = hp
        self.__damage = dm
        self.__color_of_the_banner = color

    @property
    def health(self):
        return self.__health

    def decorator_luck(func):
        def luck1(self):
            luck = rd.randint(-10, 110)
            coefficient = 1
            if 0 < luck <= CONST_N:
                print("Удача, атака увеличивается в ", CONST_M, " раз")
                coefficient = CONST_M
            elif luck < 0:
                print("Большая неудача, атака уменьшается в 3 раза")
                coefficient = 1 / 3
            elif 108 > luck > 100:
                print("Большая удача, атака увеличивается в 3 раза")
                coefficient = 3
            elif luck > 108:
                print("Фаталити, атака увеличивается в 20 раз")
                coefficient = 20

            return func(self) * coefficient

        return luck1

    @property
    @decorator_luck
    def damage_luck(self):
        return self.__damage

    @property
    def damage(self):
        return self.__damage

    @property
    def color_of_the_banner(self):
        return self.__color_of_the_banner

    # метод печати экземпляра класса в print()
    def __str__(self):
        string_line = f"Knight(health = {self.__health}, damage= {self.__damage}, color_of_the_banner= {self.__color_of_the_banner})"
        return string_line
