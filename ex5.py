# Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел. У пользователя
# необходимо запрашивать новый элемент рейтинга. Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.


my_list = [10, 7, 5, 3, 3, 2]
element = int(input('Введите новый элемент рейтинга: '))

if element in my_list:
    position = my_list.index(element)
    my_list.insert(position, element)
elif element not in my_list:
    count = 0
    if element > my_list[0]:
        my_list.insert(0, element)
    elif my_list[-1] > element:
        my_list.append(element)
    else:
        for i in my_list:
            if my_list[count] > element > my_list[count + 1]:
                position = my_list.index(i)
                my_list.insert(position + 1, element)
                break
            count += 1

print(my_list)

