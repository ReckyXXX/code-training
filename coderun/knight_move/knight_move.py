"""
    Difficulty: [Easy]

Дана прямоугольная доска N×M
N×M (N строк и M столбцов). 
В левом верхнем углу находится шахматный конь, которого необходимо переместить в правый нижний угол доски. 
В данной задаче конь может перемещаться на две клетки вниз и одну клетку вправо или на одну клетку вниз и две клетки вправо.

Необходимо определить, сколько существует различных маршрутов, ведущих из левого верхнего в правый нижний угол.

Формат ввода
Входной файл содержит два натуральных числа N и M (1 ⩽ N,M ⩽ 50) 

Формат вывода
В выходной файл выведите единственное число — количество способов добраться конём до правого нижнего угла доски.

Ограничения
Ограничение времени
1 с
Ограничение памяти
64 МБ
"""

import sys

# moves are "paths"
def calculate_knight_moves_count(N, M):
    return calculate_position_moves_count(1, 1, N, M)


def calculate_position_moves_count(n, m, N, M):
    if (n < 1 or n > N or m < 1 or m > M):
        return 0
    if (n == N and m == M):
        return 1
    result = 0
    result += calculate_position_moves_count(n + 2, m + 1, N, M)
    result += calculate_position_moves_count(n + 1, m + 2, N, M)
    return result
    

def main():
    N, M = [int(x) for x in input().split()[:2]]
    moves_count = calculate_knight_moves_count(N, M)
    print(moves_count)


if __name__ == '__main__':
    main()