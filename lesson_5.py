# Задание 1 Упражнение 5

import os
user_file = r"user_file.txt"
if os.path.exists("."):
    if os.path.exists(user_file):
        os.remove(user_file)
    _id = False
    value = ""
    try:
        with open(user_file, "a") as ufile:
            while not _id:
                value = input("Введите значение\n")
                if ufile.writable():
                    ufile.write(f"{value}\n")
                    if value == "":
                        break
                else:
                    print("Файл нельзя создать")
                    break
    except:
        print("Ошибка")

# Задание 2 Упражнение 5

import os
test_file = r"test2exapmple.txt"
if os.path.exists("."):
    if os.path.exists(test_file):
        os.remove(test_file)
    try:
        strokes = ["Строка1\n",
                "Строка2\n",
                "Строка3\n"]
        with open(test_file, "w+") as txt_test:
            txt_test.writelines(strokes)
        if os.path.exists(test_file):
            new_strokes = open(test_file)
            array_stroke = new_strokes.readlines()
            print(f"колличество строк: {len(array_stroke)}")
            for line in array_stroke:
                strokes = line.split()
                print(f"для строки: {line} {len(strokes)} слов")
            new_strokes.close()
    except:
        print("ошибка")

# Задание 4 Упражнение 5

import os
import random
test_file = r"test5example.txt"
if os.path.exists(test_file):
    os.remove(test_file)
try:
    with open(test_file, "w+") as _file:
        data = [random.randint(0,20) for x in range(100, 150)]
        _value: str = ""
        for value in data:
            _value = _value + " " + str(value)
        _file.write(_value)
        print(f"Результат генерации: \n{_value}\n")
except:
    print("Ошибка в генерации или записи данных")
try:
    with open(test_file) as _file:
        s_data = _file.read().split()
        s_data = list((map(lambda x: int(x), s_data)))
        print(f"Сумма всех чисел:\n{sum(s_data)}")
except:
    print("Ошибка в десериализации или расчете")

# Задание 7 Упражнение 5

import os
import statistics
import json
test_file_first = r"test7example.txt"
if os.path.exists(test_file_first):
    os.remove(test_file_first)
    with open(test_file_first, "a") as file_first:
        data = ["Microsoft ООО 10000 5000", "Eldis AO 20000 11000", "Apple Corp 19000 12000"]
        for value in data:
            file_first.write(f"{value}\n")
with open(test_file_first) as file_first:
        data = []
        pribil = []
        average_pribil = int()
        for value in file_first.readlines():
            data_line = []
            for val in value.split():
                data_line.append(val)
            data.append(data_line)
            print(f"прибыль фирмы: {data_line[0]} = {(int(data_line[2]) - int(data_line[3]))}")
            if (int(data_line[2]) - int(data_line[3])) > 0:
                pribil.append((int(data_line[2]) - int(data_line[3])))
            average_pribil = statistics.mean(pribil)
        print(f"средняя выручка фирм: {average_pribil}")
        if os.path.exists("test_file_json.json"):
            os.remove("test_file_json.json")
        _json = [data, {"Средняя прибыль": average_pribil}]
        with open("test_file_json.json", "w") as jsons:
            json.dump(_json, jsons)
        with open("test_file_json.json") as jsons:
            _json = None
            _json = json.load(jsons)
            print(f"Десериализация выполнена успешно\n{_json}")
