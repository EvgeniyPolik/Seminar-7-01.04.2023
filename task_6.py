"""
Задача 6: Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6), которая принимает в качестве
аргумента функцию, вычисляющую элемент по номеру строки и столбца. Аргументы num_rows и num_columns указывают число
строк и столбцов таблицы, которые должны быть распечатаны. Нумерация строк и столбцов идет с единицы (подумайте,
почему не с нуля). Примечание: бинарной операцией называется любая операция, у которой ровно два аргумента, как,
например, у операции умножения.

*Пример:*

**Ввод:** `print_operation_table(lambda x, y: x * y) `
**Вывод:**

1 2 3 4 5 6

2 4 6 8 10 12
3 6 9 12 15 18
4 8 12 16 20 24
5 10 15 20 25 30
6 12 18 24 30 36
"""


class OperationTable:
    def __init__(self, operation, num_rows, num_columns):
        self.operation = operation
        self.num_rows = num_rows
        self.num_columns = num_columns

    def __str__(self):
        result = ''
        for i in range(self.num_rows):
            for j in range(self.num_columns):
                result += str(eval('(lambda x, y: ' + self.operation + f')({i + 1}, {j + 1})')).rjust(3, ' ')
            result += '\n'
        return result


def print_operation_table(operation, num_rows=6, num_columns=6):
    obj = OperationTable(operation, num_rows, num_columns)
    print(obj)


oper = input('Введите функцию, бинарную функцию (Напр: x * y): ')
print_operation_table(oper)

