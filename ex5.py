# Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами. Программа
# должна подсчитывать сумму чисел в файле и выводить ее на экран.


with open('ex5_text.txt', 'w+', encoding='utf-8') as f:
    numbers = input('Введите набор чисел: ')
    f.write(numbers)
    num_sum = sum(map(int, numbers.split()))
    print(num_sum)