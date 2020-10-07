# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные. При этом английские
# числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.


with open('ex4_text.txt', encoding='utf-8') as f:
    new_file = []
    for line in f:
        string = line.strip()
        print(string)
        new_list = string.split(' ')
        new_list.remove(new_list[0])
        if '1' in new_list:
            new_list.insert(0, "Один")
        elif '2' in new_list:
            new_list.insert(0, "\nДва")
        elif '3' in new_list:
            new_list.insert(0, "\nТри")
        elif '4' in new_list:
            new_list.insert(0, "\nЧетыре")

        rus_string = ' '.join(new_list)

        with open('rus_file.txt', 'a', encoding='utf-8') as new_file:
            new_file.write(rus_string)

