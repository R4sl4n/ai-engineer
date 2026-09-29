import sys; sys.stdout.reconfigure(encoding='utf-8')

# Основные типы
name = "Руслан"          # str: строка
age = 30                 # int: целое число
height = 1.75            # float: дробное число
is_student = True        # bool: True или False
nothing = None           # None: "пусто"


# Коллекции
numbers = [1, 2, 3]                  # list: изменяемый список
point = (10, 20)                     # tuple: неизменяемый набор
user = {"name": "Руслан", "age": 30} # dict: пары ключ-значение
unique = {1, 2, 2, 3}                # set: только уникальные значения

print(type(name), type(age), type(numbers), type(user))
print(unique)


# f-строки: вставка значений в текст
print(f"Меня зовут {name}, мне {age}")


# Функция со значением по умолчанию
def greet(name: str, greeting: str = "Салам") -> str:
    return f"{greeting}, {name}!"

print(greet("Ruslan"))
print(greet("Ruslan", greeting="Hey"))


for n in numbers:
    if n % 2 == 0:
        print(n, 'Четное')
    else:
        print(n, 'Нечетное')

   
    