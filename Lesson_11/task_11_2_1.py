# 2. Усложнение:
# Сформируйте для класса-исключения сообщение, включающее делимое и делитель
# и сообщение о невозможности деления. Для этого придется наполнить исключение данными.

class DivZeroException(Exception):
    def __init__(self, arg1, arg2):
        self.arg1 = arg1
        self.arg2 = arg2

    def __str__(self):
        return f'{self.arg1}/{self.arg2} Ошибка, деление на ноль!'


def my_division(arg1, arg2):
    # Вариант 2 с проверкой результата после деления
    try:
        result = arg1 / arg2
    except ZeroDivisionError:
        raise DivZeroException(arg1, arg2)
    else:
        print(f'{arg1}/{arg2} =', result)
    return result


try:
    my_division(8, 0)
except DivZeroException as err:
    print(err)

try:
    my_division(8, 4)
except DivZeroException as err:
    print(err)
