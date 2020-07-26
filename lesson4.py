### 1 задание 4 урока.

import sys
name, work, hour, premium = sys.argv
salary = (int(work) * int(hour)) + int(premium)
print(salary)

### 2 задание 4 урока.

import random
random_value = [int(i) for i in list((range(300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55)))]
random.shuffle(random_value)
print(random_value)

def my_func(list):
    base_list = list[0]
    current_list = []
    for i in list:
        if i > base_list:
            current_list.append(x)
    return current_list
new_list = my_func(random_value)
print(new_list)

### 3 задание 4 урока.

numbers = [i for i in range(20, 241) if i % 20 == 0 or i % 21 == 0]
print(numbers)

### 5 задание 4 урока.

from functools import reduce
form_list = [i for i in list(range(100, 1001))]
value = reduce(lambda x,y: x * y, form_list )
print(form_list)
print(value)
