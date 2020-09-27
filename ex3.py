# Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень). Напишите решения через list и через dict.


month = 0
season_ls = ['winter', 'spring', 'summer', 'fall']
season_dict = {1 : 'winter', 2 : 'spring', 3 : 'summer', 4 : 'fall'}
while month not in range(1,12):
    month = int(input('Введите месяц от 1 до 12: '))
    continue
if month in range(3,5):
    print(season_ls[1])
    print(season_dict.get(2))
elif month in range(6,8):
    print(season_ls[2])
    print(season_dict.get(3))
elif month in range(9,11):
    print(season_ls[3])
    print(season_dict.get(4))
else:
    print(season_ls[0])
    print(season_dict.get(1))


