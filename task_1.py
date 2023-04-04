"""
Задание 1.

Создать класс TrafficLight (светофор)
и определить у него один приватный атрибут color (цвет) и публичный метод running (запуск).
В рамках метода running реализовать переключение светофора в режимы:
красный, желтый, зеленый. Продолжительность первого состояния (красный)
составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) —
на ваше усмотрение.
Для имитации "горения" каждого цвета испольщуйте ф-цию sleep модуля time
Переключение между режимами должно осуществляться только
в указанном порядке (красный, желтый, зеленый).
Проверить работу примера, создав экземпляр и вызвав описанный метод.
"""


import os
import time



class TrafficLight:
    __color = ('red', 7)

    def running(self):
        colors = [('red', 7), ('yellow', 3), ('green', 7)]
        current_light = 0
        while True:
            os.system('cls')
            print(f'Текущий цвет: {self.__color[0]}')
            time.sleep(self.__color[1])
            if current_light < 2:
                current_light += 1
            else:
                current_light = 0
            self.__color = colors[current_light]


traffic_light = TrafficLight()
traffic_light.running()

