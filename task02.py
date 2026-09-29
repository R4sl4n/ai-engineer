import sys; sys.stdout.reconfigure(encoding='utf-8')

# Функция square(n: int) -> int, возвращает квадрат числа.
# Функция count_even(numbers: list[int]) -> int, возвращает количество чётных чисел в списке.
# Функция make_user(name: str, age: int) -> dict, возвращает словарь пользователя.

def square(n: int) -> int:
    return n * n



def count_even(numbers: list[int]) -> int:
    count = 0
    for n in numbers:
        if n % 2 == 0:
            count += 1
    return count


def make_user(name: str, age: int) -> dict:
    return {"name": name, "age": age}
    

print(square(2))   
print(count_even([1,2,3,4,6]))
print(make_user("Ruslan", 30))