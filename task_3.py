"""
Задание 3.

Реализовать базовый класс Worker (работник),
в котором определить публичные атрибуты name, surname, position (должность),
и защищенный атрибут income (доход). Последний атрибут должен ссылаться
на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
Создать класс Position (должность) на базе класса Worker. В классе Position реализовать публичные методы
получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные,
проверить значения атрибутов, вызвать методы экземпляров).
П.С. попытайтесь добить вывода информации о сотруднике также через перегрузку str
str(self) - вызывается функциями str, print и format. Возвращает строковое представление объекта.
"""


class Worker:
    _income = {'wage': 0, 'bonus': 0}

    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position


class Position(Worker):
    def __init__(self, name, surname, position, income):
        super().__init__(name, surname, position, income)
        self._income = income

    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        return self._income.get('wage', 0) + self._income.get('bonus', 0)

    def __str__(self):
        return f'Имя сотрудника: {self.get_full_name()}, должность: {self.position}, доход: {self.get_total_income()}'


cleaner_solary = {'wage': 10000, 'bonus': 1500}
cleaner = Position('Василий', 'Петров', 'уборщик', cleaner_solary)
print(cleaner.get_full_name())
print(cleaner.get_total_income())
print(cleaner)
