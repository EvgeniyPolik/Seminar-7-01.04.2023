"""
Задание 2.

Реализовать класс Road (дорога), в котором определить защищенные атрибуты:
length (длина в метрах), width (ширина в метрах).
Значения данных атрибутов должны передаваться при создании экземпляра класса.
Реализовать публичный метод расчета массы асфальта, необходимого для покрытия
всего дорожного полотна.
Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв
метра дороги асфальтом, толщиной в 1 см * число м толщины полотна.
Массу и толщину сделать публичными атрибутами.
Проверить работу метода.

Например: 20м*5000м*25кг*0.05м = 125000 кг = 125 т
"""


class Road:
    mass = 25

    def __init__(self, lenght_in_m, width_in_m, depth_in_m):
        self._lenght_in_m = lenght_in_m
        self._width_in_m = width_in_m
        self._depth_in_m = depth_in_m

    def get_mass_asphalt(self):
        return self.mass * self._width_in_m * self._lenght_in_m * self._depth_in_m


road = Road(5000, 20, 0.05)
print(f'Полученная масса асфальта: {road.get_mass_asphalt()} кг или {road.get_mass_asphalt() / 1000} тонн')
