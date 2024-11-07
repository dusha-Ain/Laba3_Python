# Класс «Рыцарь» с полями «здоровье», «урон» и «цвет знамени». Знамя может иметь
# один из семи цветов радуги — при создании очередного рыцаря цвет знамени
# не запрашивается, а автоматически выбирается «следующим» (т.е. к-о-ж-з-г-с-ф-к…).
# Декоратор «удача» с шансом N% увеличивает результат в M раз. Декорировать геттер
# урона. Задача должна мочь ввести двух рыцарей и устроить поединок

from Knight import Knight
import random as rd
import time


CONST_COLORS = ['к', 'о', 'ж', 'з', 'г', 'с', 'ф']
COLOR_index = None


def main_menu():
    print("\n\t\t[Управление рыцарями]")
    print("1 - Создать рыцаря(при создании номер вернётся к последнему созданному рыцарю)")
    print("2 - Получить параметр здоровья")
    print("3 - Получить парметр атаки")
    print("4 - Получить значения цвета знамени")
    print("5 - Посмотреть состав рыцарей")
    print("6 - Вернуться к рыцарю под номером")
    print("7 - Поединок рыцарей")
    print("8 - Завершить программу")


def color_next():
    global COLOR_index

    if COLOR_index + 1 == len(CONST_COLORS):
        COLOR_index = 0
        color = "к"
    else:
        color = CONST_COLORS[COLOR_index + 1]
        COLOR_index += 1
    return color


# функция для записи данных из файла
def input_from_file(array):
    with open("data.txt") as file:
        global COLOR_index
        while True:
            hp = file.readline()
            dm = file.readline()
            if COLOR_index is None:
                color = file.readline().replace("\n", "")
                COLOR_index = CONST_COLORS.index(color)
            else:
                color = color_next()
            if not hp or not dm:
                break
            array.append(Knight(int(hp), int(dm), color))


# создание рыцаря при помощи консоли
def write_console_knight():
    print("Введите в числовм значении здоровье рыцаря: ", end="")
    hp = int(input())
    print("Введите в числовм значении урон рыцаря: ", end="")
    dm = int(input())

    global COLOR_index
    if COLOR_index is None:
        print("Введите в символьном значении цвет знамени(т.е. к-о-ж-з-г-с-ф): ", end="")
        color = input()
        COLOR_index = CONST_COLORS.index(color)
    else:
        color = color_next()

    return Knight(hp, dm, color)


# функция для записи данных в файл
def print_in_file(array, num):
    file = open('ans.txt', 'w')
    if num < 0:
        file.write("Отряд пуст")
    else:
        for i in array:
            file.write(str(i) + "\n")

    file.close()


def battle(warrior1, warrior2):
    t = False
    while not t:
        print("\n\t[ Menu battle ]")
        print("1 - распечатать 1 - ого рыцаря")
        print("2 - распечатать 2 - ого рыцаря")
        print("3 - Начать битву\n")
        choice_battle = int(input())
        match choice_battle:
            case 1:
                print(warrior1)
            case 2:
                print(warrior2)
            case 3:
                t = True
    tmp_health1 = warrior1.health
    tmp_health2 = warrior2.health
    while t:
        print("Здоровье рыцарей: %.2f" % tmp_health1, " %.2f" % tmp_health2)
        start = rd.randint(1, 200)
        time.sleep(3)
        if start % 8 == 0 or start % 3 == 0:
            print("Атакует 1 - ый рыцарь")
            attack = warrior1.damage_luck
            print("Атака равна = %2.f" % attack)
            tmp_health2 -= attack
            time.sleep(5)
        elif start % 2 == 0 or start % 7 == 0:
            print("Атакует 2 - ой рыцарь")
            attack = warrior2.damage_luck
            print("Атака равна = %2.f" % attack)
            tmp_health1 -= attack
            time.sleep(5)
        else:
            print("Воины держат оборону")
            time.sleep(3)
        if tmp_health1 <= 0 or tmp_health2 <= 0:
            t = False
            if tmp_health1 <= 0:
                print("Победил 2 - ой рыцарь")
            else:
                print("Победил 1 - ый рыцарь")


# массив для хранения всех созданных рыцарей
array_of_knights = []

# порядковый номер текущего рыцаря
num_knigts = -1
choice = 0

while choice < 8:
    # интерфейс пользователя
    main_menu()

    # переменная отвечающая за выбор пользователя
    choice = int(input())

    match choice:
        case 1:
            print("Данные считывать с ...\n1 - с консоли\n2 - из файла")
            inp = int(input())
            if inp == 1:
                if num_knigts != -1 and num_knigts < len(array_of_knights) - 1:
                    num_knigts = len(array_of_knights) - 1
                array_of_knights.append(write_console_knight())
                num_knigts += 1
            else:
                input_from_file(array_of_knights)
                num_knigts = len(array_of_knights) - 1
        case 2:
            if num_knigts < 0:
                print("Отряд пуст")
            else:
                print("Health = ", array_of_knights[num_knigts].health)
        case 3:
            if num_knigts < 0:
                print("Отряд пуст")
            else:
                print("Damage = ", array_of_knights[num_knigts].damage)
        case 4:
            if num_knigts < 0:
                print("Отряд пуст")
            else:
                print("color of the banner = ", array_of_knights[num_knigts].color_of_the_banner)
        case 5:
            print("Данные вывести в ...\n1 - в консоль\n2 - в файл")
            inp = int(input())
            if inp == 1:
                if num_knigts < 0:
                    print("Отряд пуст")
                else:
                    i = 1
                    for knigt in array_of_knights:
                        print(f'{i}.%15s ' % knigt)
                        i += 1
            else:
                print_in_file(array_of_knights, num_knigts)
        case 6:
            print("Введите номер рыцаря, к которому хотите вернуться: ", end="")
            tmp_num_knigts = int(input()) - 1
            if tmp_num_knigts < 0 or tmp_num_knigts > len(array_of_knights) - 1:
                print("Некорректный номер")
            else:
                num_knigts = tmp_num_knigts
                print("Рыцарь найден")
        case 7:
            print("Введите номера рыцарей, которые будут сражаться")
            print("Номер 1 - ого рыцаря: ", end="")
            num1 = int(input()) - 1
            print("Номер 2 - ого рыцаря: ", end="")
            num2 = int(input()) - 1
            count_knights = len(array_of_knights) - 1
            if num1 == num2 or num1 > count_knights or num1 < 0 or num2 < 0 or num2 > count_knights:
                print("Некорректный ввод")
            else:
                battle(array_of_knights[num1], array_of_knights[num2])
        case 8:
            chocie = 7
