# Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
# количества слов в каждой строке.


with open('ex2_text.txt') as f:
    line_counter = 0
    for line in f:
        print(line.strip())
        listline = line.split(' ')
        words = len(listline)
        print(f'Количество слов в строке: {words}')
        line_counter += 1
    print(f'Количество строк в файле: {line_counter}')
