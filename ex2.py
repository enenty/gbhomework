# Для списка реализовать обмен значений соседних элементов, т.е.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

my_list = []
list_len = int(input('Введите количество элементов списка: '))
count = 0
index = 0
while count < list_len:
    my_list.append(input('Введите элемент списка: '))
    count += 1

for i in my_list:
    length = len(my_list)
    if index < length - 1:
        my_list[index], my_list[index+1] = my_list[index+1], my_list[index]
        index += 2

print(my_list)
