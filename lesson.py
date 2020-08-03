# 1 задание 6 урока

from time import sleep
class TrafficLight:
    sample_color = ["red", "yellow", "green"]
    timer = {sample_color[0]: 7, sample_color[1]: 2, sample_color[2]: 2}

    if sample_color == ["red", "yellow", "green"]: #B
        def svetofor(color_selector):
            print(color_selector.sample_color[0])
            sleep(color_selector.timer[color_selector.sample_color[0]])
            print(color_selector.sample_color[1])
            sleep(color_selector.timer[color_selector.sample_color[1]])
            print(color_selector.sample_color[2])
            sleep(color_selector.timer[color_selector.sample_color[2]])
    else:
        print("Вы поменяли параметры")
newTrafficLight = TrafficLight().svetofor()

# 2 задание 6 урока

class Road:
    length: int
    width: int
    mass: int
    def __init__(param, length_m, width_m, mass_s):
        param.length = length_m
        param.width = width_m
        param.mass = mass_s
    def weight(param):
        print(f"Длина {param.length} ширина {param.width} и высота{param.mass}, вес: {param.length*param.width*param.mass/100*2.5}")
count = Road(650, 25, 8).weight_road()

# 3 задание 6 урока

class Worker:
    name: str
    surname: str
    position: str
    wage: int
    bonus: int
    income = {}
    def __init__(param, name, surname, position, wage, bonus):
        param.name = name
        param.surname = surname
        param.position = position
        param.wage = wage
        param.bonus = bonus
        param.income = {"wage": wage, "bonus": bonus}
class Position(Worker):
    def get_full_name(param):
        print(param.name + " " + param.surname)
    def get_total_income(param):
        print(f"{param.wage + param.bonus}")
Urich = Position("Сан", "Юрьич", "Инженер", 45000, 5000)
Urich.get_full_name()
Urich.get_total_income()

# 7 задание 6 урока

class Stationery:
    title: str = "Example"
    def draw(param):
        print("отрисовка")
class Pen(Stationery):
    def draw(param):
        print("ручка")
class Pencil(Stationery):
    def draw(param):
        print("карандаш")
class Handle(Stationery):
    def draw(param):
        print("маркер")
example_first = Stationery()
example_first.draw()

example_second = Pen()
example_second.draw()

example_third = Pencil()
example_third.draw()

example_fourth = Handle()
example_fourth.draw()
