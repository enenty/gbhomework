# Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника. В расчете
# необходимо использовать формулу: (выработка в часах * ставка в час) + премия. Для выполнения расчета для конкретных
# значений необходимо запускать скрипт с параметрами.


from sys import argv


name, hours, rate, bonus = argv

try:
    print('Трудовые часы: ', hours)
    print('Ставка в час: ', rate)
    print('Премия: ', bonus)
    print('Заработная плата сотрудника', int(hours) * int(rate) + int(bonus))
except ValueError:
    print('Нечисловые значения параметров')



