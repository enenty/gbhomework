# Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый,
# зеленый. Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды,
# третьего (зеленый) — на ваше усмотрение. Переключение между режимами должно осуществляться только в указанном
# порядке (красный, желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод.

from time import sleep
from itertools import cycle


class TrafficLight:
    def __init__(self):
        self.__color = ['Red', 'Yellow', 'Green']

    def running(self):
        for color in cycle(self.__color):
            if color == 'Red':
                print(color)
                sleep(5)
            elif color == 'Yellow':
                print(color)
                sleep(2)
            else:
                print(color)
                sleep(10)


traffic = TrafficLight()
traffic.running()
