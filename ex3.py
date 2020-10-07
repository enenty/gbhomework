# Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов. Определить,
# кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников. Выполнить подсчет средней величины
# дохода сотрудников.


with open('ex3_text.txt') as f:
    counter = 0
    average = 0
    average_list = []
    employees = []
    for line in f:
        worker = line.split(' ')
        if int(worker[1]) < 20000:
            employees.append(worker[0])

        average_list.append(int(worker[1]))
        counter += 1
    average = sum(average_list) / counter
    employees = ', '.join(employees)
    print('Сотрудники с зп меньше 20тыс: ', employees)
    print('Средняя зарплата сотрудников: ', int(average))