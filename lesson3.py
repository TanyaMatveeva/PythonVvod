### 1 задание 3 урока
def divNumbers(number1, number2) :
    try:
        if number2 == 0:
            print('На ноль делить нельзя')
        else:
            return number1 / number2
    except:
       print('вы ввели некорректное значение')

requestNum1 = int(input('Введите первое число: '))
requestNum2 = int(input('Введите второе число: '))
print(f'Результат деления: {divNumbers(requestNum1, requestNum2)}')



### 2 задание 3 урока
def userData(name, secondName, birthYear, residenceCity, email, phone) :
    return (f'Пользователь {name} {secondName}, проживающий в городе {residenceCity}, родился в {birthYear} году. Его телефон: {phone} и email: {email}')
print(userData(name='Иван', secondName='Иванов', birthYear=1980, email='ivanivanov@mail.ru',phone=88005553555, residenceCity='Москва'))



### 3 задание 3 урока
# 1 вариант, топорный
def my_func(argument1, argument2, argument3) :
    if argument1 >= argument2 >= argument3 or argument2 >= argument1 >= argument3:
        return argument1 + argument2
    if argument2 >= argument3 >= argument1 or argument3 >= argument2 >= argument1:
        return argument2 + argument3
    if argument3 >= argument1 >= argument2 or argument1 >= argument3 >= argument2:
        return argument3 + argument1
print(f'Результат сложения двух максимальных чисел {my_func(5, 10, 15)}')

# 2 вариант
def my_func(argument1, argument2, argument3):
    minValue = min(argument1, argument2, argument3)
    return (argument1 + argument2 + argument3) - minValue
print(f'Результат сложения двух максимальных чисел {my_func(50, 40, 8)}')



### 4 задание 3 урока
# Не смогла реализовать также проверку на отрицательность/положительность вместе с проверками на тип данных, так как изначально усложнила себе задачу вместо обработки конкретных цифр решила запрашивать их у пользователя.
# 1 вариант
x, y = float(input('Введите положительное действительное число x: ')), int(input('Введите целое отрицательное число y: '))
def my_func1(x, y):
    if x > 0 and y < 0:
        return x**y
    else:
        print('Вы ввели неправильные числа')

# 2 вариант
def my_func2(x,y):
    numbery = abs(y)-1
    numberx = x
    while numbery != 0:
        numberx = x * numberx
        numbery -= 1
    if y < 0:
        numberx = 1 / numberx
    if y % 2 != 0:
        numberx = numberx * -1
    print(numberx)
print(my_func2(x,y))



## 5 задание 3 урока
splitNumbers = input('Введите строку чисел разделенных пробелами: ')
sumNumbers = 0
sumNumbers = (int(i) for i in str(splitNumbers)):
sumNumbers += i
print(sumNumbers)
def isNumeric(num):
    try:
        a = int(x)
        return True
    except:
        return False
sumNumbers = 0
numbers = ''
while numbers != 'stop':
    try:
        numbers = input('Введите строку чисел разделенных пробелами: ')
        splitNumbers = [x for x in numbers.split(' ')]
        print(splitNumbers)
        for x in splitNumbers:
            if (isNumeric(x)):
                sumNumbers += int(x)
        print(sumNumbers)
    except ValueError:
        print('Вы ввели неправильное значение')



### 6 задание 3 урока
def int_func(word):
    return str.capitalize(word)
perem1 = input('Введите слова: ')
words = perem1.split(' ')
words2 = [int_func(i) for i in words]
dots = ' '
print(dots.join(words2))
