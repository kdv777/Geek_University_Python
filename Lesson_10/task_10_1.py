# Техническое задание:
#
# Элементы матрицы - целые числа(для простоты)
# Данные в матрице хранятся как список списков целых чисел.
# Реализовать перегрузку метода 'str()' для вывода матрицы в привычном виде - как в примере.
# Выравнивание чисел не обязательно, но желательно. Метод 'str()' возвращает строку.
# Реализовать перегрузку метода 'add()' для сложения двух объектов класса Matrix (двух матриц).
# Результатом сложения должна быть новая матрица. Метод 'add()' возвращает новую матрицу.
# Исходные матрицы остаются неизменными. Сложение элементов матриц выполнять поэлементно.
# Первый элемент первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.
# Поэтому количество строк в обоих матрицах должно быть одинаковым. Аналогично со столбцами.
# Подумайте о проверках корректности данных при создании матрицы и при их сложении.
# Какие могут быть ошибки, когда мы работаем со списком списков.
# Что делают операторы (например сложения), когда выполнить операцию невозможно?
# Создать несколько матриц разного размера.
# Вывести их с помощью print
# Выполнить сложение матриц и вывести результат сложения.
# Подтвердить, что после сложения полученный объект имеет тип матрица.

class Matrix:

    # matrix1 = [[31, 32], [37, 43], [51, 46]]
    # matrix2 = [[17, 15], [21, 32], [11, 23]]
    matrix_str = ''

    def __init__(self, matrix=[]):
        self.matrix = matrix

    def __str__(self):
        for el in self.matrix:
            self.matrix_str = f'{self.matrix_str} | {str(el)} | \n'
        return self.matrix_str

    def __add__(self, other):
        # Реализовать исключение!
        if len(self.matrix) != len(other.matrix):
            raise ValueError("Incorrect data for Matrix initialization: not equal lenght of lists")
        try:
            self.result_matrix = self.matrix.copy()
            for i in range(len(self.matrix)):
                if len(self.matrix[i]) != len(other.matrix[i]):
                    raise ValueError('Wrong matrixs')
                for j in range(len(self.matrix[0])):

                    self.result_matrix[i][j] = self.matrix[i][j] + other.matrix[i][j]
            # Создаем объект того же класса
            # self.matrix = Matrix(self.result_matrix)
            self.matrix = self.__class__(self.result_matrix)
        except IndexError:
            print('Error')

        return self.matrix


a = Matrix([[31, 32], [37, 43], [51, 46]])
b = Matrix([[17, 15], [21, 32], [11, 23]])
e = Matrix([[1, 1, 2], [2, 1, 1], [4, 5, 6]])
# g = Matrix([[3, 4, 5], [1, 7, 1], [2, 2, 1]])
g = Matrix([[3, 4, 5, 7], [1, 7, 1]])
print(a)
print(b)
z = a + b
print(z)
print(type(z))
print(e)
print(g)
x = e + g
# print(x)
