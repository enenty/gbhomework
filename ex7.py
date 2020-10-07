# Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
# название, форма собственности, выручка, издержки.
#
# Пример строки файла: firm_1 ООО 10000 5000.
#
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
# а также словарь со средней прибылью. Если фирма получила убытки, также добавить ее в словарь (со значением
# убытков).
#
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
#
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
#
# Пример json-объекта: [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]


import json


with open('ex7_text.txt', encoding='utf-8') as f:
    file_dict, average_profit = {}, {}
    firm_count, profit = 0, 0
    firm_profits = []
    for line in f:
        line_ls = line.split()
        firm = line_ls[0]
        income = int(line_ls[2]) - int(line_ls[3])
        file_dict[firm] = income
        if income > 0:
            firm_count += 1
            profit += income
    average_profit['average_profit'] = int(profit / firm_count)
    firm_profits = [file_dict, average_profit]
    print(firm_profits)

with open('firm_profit.json', 'w+', encoding='utf-8') as json_f:
    json.dump(firm_profits, json_f)
