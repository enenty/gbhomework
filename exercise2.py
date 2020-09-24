# Пользователь вводит время в секундах.
# Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.

time_seconds = int(input('Введите время в секундах: '))
hours = time_seconds // 3600
minutes = (time_seconds - (hours * 3600)) // 60
seconds = time_seconds - ((hours * 3600) + (minutes * 60))
seconds_string = str(seconds)
minutes_string = str(minutes)
hours_string = str(hours)
if seconds < 10:
    seconds_string = '0' + seconds_string

if minutes < 10:
    minutes_string = '0' + minutes_string

if hours < 10:
    hours_string = '0' + hours_string

print(f'Время в формате чч:мм:сс \n- - {hours_string}:{minutes_string}:{seconds_string} - -')