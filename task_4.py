"""
Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод init()), который должен
принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц: 3 на 2, 3 на 3, 2 на 4.

31 22
37 43
51 86

3 5 32
2 4 6
-1 64 -8

3 5 8 3
8 3 7 1

Следующий шаг — реализовать перегрузку метода str() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода add() для реализации операции сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица. Подсказка: сложение элементов матриц выполнять поэлементно — первый
элемент первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.
"""

class Matrix:
    def __init__(self, elements):
        if len(elements) == 0:
            raise ValueError('Emty input')
        first_len = len(elements[0])
        for el in elements:
            if first_len != len(el):
                raise ValueError('Wrong data')
        self.elements = elements

    def __str__(self):
        result = ''
        for i in self.elements:
            for j in i:
                result += str(j).rjust(3, " ")
            result += '\n'
        return result

    def __add__(self, matrix_b):
        if len(self.elements) != len(matrix_b.elements) and len(self.elements[0]) != len(matrix_b.elements[0]):
            raise ValueError('Wrong operation')
        for i in range(len(self.elements)):
            for j in range(len(self.elements[0])):
                self.elements[i][j] += matrix_b.elements[i][j]
        return self


exp_a = [[1, 2], [3, 3]]
exp_b = [[2, 1], [3, 3]]

m = Matrix(exp_a)
n = Matrix(exp_b)

print('Первая матрица:')
print(m)
print('Вторая матрица:')
print(n)
print('Результат сложения:')
print(m + n)