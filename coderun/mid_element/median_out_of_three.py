"""
    Difficulty: [Easy]
    Tags: sort

    Рассмотрим три числа 
    a
    a, 
    b
    b и 
    c
    c. Упорядочим их по возрастанию.

    Какое число будет стоять между двумя другими?

    Формат ввода
    В единственной строке записаны три целых числа 
    −1000 ≤ a,b,c ≤ 1000), числа разделены одиночными пробелами.

    Формат вывода
    Выведите число, которое будет стоять между двумя другими после упорядочивания.

    Ограничения
    Ограничение времени
    1 с
    Ограничение памяти
    256 МБ
"""

import sys


def median_out_of_three(numbers):
    numbers.sort()
    return numbers[1]


def main():
    numbers = [int(x) for x in input().split()[:3]]
    median = median_out_of_three(numbers)
    print(median)


if __name__ == '__main__':
    main()