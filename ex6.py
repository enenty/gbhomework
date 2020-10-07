# Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие
# лекционных, практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для каждого
# предмета не обязательно были все типы занятий. Сформировать словарь, содержащий название предмета и общее
# количество занятий по нему. Вывести словарь на экран.


with open('ex6_text.txt', encoding='utf-8') as f:
    file_dict = {}
    for line in f:
        string = line.strip()
        new_list = string.split(': ')
        course = new_list[0]
        new_string = new_list[1]
        new_string = new_string.replace(')', '(')  # здесь родились костыли
        new_string = new_string.replace('—', '')
        new_string = new_string.replace(' ', '')
        hours = [int(num) for num in new_string.split('(') if num.isdigit()]
        file_dict[course] = sum(hours)
    print(file_dict)
