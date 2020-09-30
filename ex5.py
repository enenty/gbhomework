# Программа запрашивает у пользователя строку чисел, разделенных пробелом. При нажатии Enter должна выводиться сумма
# чисел. Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter. Сумма вновь введенных
# чисел будет добавляться к уже подсчитанной сумме. Но если вместо числа вводится специальный символ, выполнение
# программы завершается. Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму этих
# чисел к полученной ранее сумме и после этого завершить программу.

def sum_int(my_str):
    a = list(map(int, my_str.split()))
    return sum(a)


sum_result = 0

while True:
    answer = input('Введите строку чисел, разделенных пробелом. "Q", чтобы выйти ').upper()
    answer_list = list(answer.split())

    if answer.upper() == 'Q':
        print('Финальная сумма равняется: ', sum_result)
        break
    elif 'Q' in answer_list:
        answer_list.remove('Q')
        answer = ' '.join(answer_list)
        summed = sum_int(answer)
        sum_result += summed
        print('Сумма чисел равна: ', sum_result)
        break
    else:
        summed = sum_int(answer)
        sum_result += summed
        print('Сумма чисел равна: ', sum_result)




