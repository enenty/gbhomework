# Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (
# булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась,
# повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый
# класс метод show_speed, который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar
# переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться
# сообщение о превышении скорости.
#
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам,
# выведите результат. Выполните вызов методов и также покажите результат.

class Car:
    def __init__(self, name, color, speed, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'{self.name} is running'

    def stop(self):
        return f'{self.name} stopped'

    def turn(self, direction):
        return f'{self.name} turned {direction}'

    def show_speed(self):
        return self.speed

    def is_police_car(self):
        if self.is_police == True:
            return f'{self.name} is a police car'
        else:
            return f'{self.name} is not a police car'



class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return f'Warning! {self.name} is speeding at {self.speed}km/h'
        else:
            return f"{self.name}'s speed is {self.speed}km/h"

class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return f'Warning! {self.name} is speeding.'
        else:
            return f"{self.name}'s speed is {self.speed}km/h"

class SportsCar(Car):
    def show_speed(self):
        return f"{self.name}'s speed is {self.speed}km/h"

class PoliceCar(Car):
    def __init__(self, name, color, speed, is_police=True):
        super().__init__(self, name, color, speed)
        self.is_police = is_police
        self.name = name
        self.color = color
        self.speed = speed



honda = TownCar('Honda Civic', 'black', 77)
kamaz = WorkCar('Kamaz truck', 'white', 38)
ferrari = SportsCar('Ferrari F40', 'red', 120)
dodge = PoliceCar('Dodge Charger', 'blue', 60)
print(honda.go())
print(honda.turn('right'))
print(honda.show_speed())
print(kamaz.go())
print(kamaz.turn('left'))
print(kamaz.show_speed())
print(kamaz.stop())
print(ferrari.go())
print(ferrari.show_speed())
print(ferrari.is_police_car())
print(dodge.is_police_car())
print(dodge.name)



