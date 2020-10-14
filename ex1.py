# Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), который должен
# принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц вы найдете в методичке.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц).
# Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки
# первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.


class Matrix:
    def __init__(self, input_matrix):
        self.input_matrix = input_matrix
        self.output_matrix = []

    def __add__(self, other):
        for row_self, row_other in zip(self.input_matrix, other.input_matrix):
            self.output_matrix.append([x + y for x, y in zip(row_self, row_other)])
        return '\n'.join(map(str, (' '.join(map(str, el)) for el in self.output_matrix)))

    def __str__(self):
        return '\n'.join(map(str, (' '.join(map(str, el)) for el in self.input_matrix)))


mat = Matrix([[31, 22],
              [37, 43],
              [51, 86]])

mat_extra = Matrix([[92, 138],
                    [33, -3],
                    [-11, -36]])

mat2 = Matrix([[3, 5, 32],
               [2, 4, 6],
               [-1, 64, -8]])

mat3 = Matrix([[3, 5, 8, 3],
               [8, 3, 7, 1]])

print(mat, mat2, mat3, 'Сложение матриц: ', mat + mat_extra, sep='\n\n')

