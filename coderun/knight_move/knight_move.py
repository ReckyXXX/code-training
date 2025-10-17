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
    position_path_map = dict()
    return calculate_position_moves_count((1, 1), N, M, position_path_map)


def calculate_position_moves_count(position, N, M, position_path_map):
    if position in position_path_map:
        return position_path_map[position]

    n = position[0]
    m = position[1]
    if (n < 1 or n > N or m < 1 or m > M):
        return 0
    if (n == N and m == M):
        return 1

    path1Start = (n + 2, m + 1)
    path1Count = calculate_position_moves_count(path1Start, N, M, position_path_map)
    position_path_map[path1Start] = path1Count

    path2Start = (n + 1, m + 2)
    path2Count = calculate_position_moves_count(path2Start, N, M, position_path_map)
    position_path_map[path2Start] = path2Count
    return path1Count + path2Count
    

def main():
    N, M = [int(x) for x in input().split()[:2]]
    moves_count = calculate_knight_moves_count(N, M)
    print(moves_count)


if __name__ == '__main__':
    main()