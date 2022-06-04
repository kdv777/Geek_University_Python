# 4. Реализовать проект «Операции с комплексными числами».
# Техническое задание:
#
# Создайте класс «Комплексное число». Комплексное число - это упорядоченная пара чисел, например x,y.
# Для простоты числа берем только целые.
# Перегрузите методы(операторы) сложения/вычитания и умножения комплексных чисел (три метода).
# Правила сложения/умножения можно найти в сети.
# Перегрузите метод 'str' для вывода числа в виде x + yj, где x,y - атрибуты.
# Попробуйте учесть, что y может быть отрицательным.
# Создайте экземпляры класса (комплексные числа), выполните сложение/вычитание/умножение созданных экземпляров.
# Выведите на экран результат.
# Убедитесь, что операторы возвращают объект нужного типа.
# Встроенным типом данных complex пользоваться нельзя. Найдите в интернете описание правил сложения/вычитания
# и умножения комплексных чисел.
# При переопределении операторов помним, что возвращается новый объект, Аргументы остаются неизменными.

class Complex:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        # Учитываем, что b может быть отрицательным.
        if self.b < 0:
            return f'{self.a}{self.b}j'
        else:
            return f'{self.a}+{self.b}j'

    def __add__(self, other):
        # (a + b i) + (c + d i) = (a + c) + (b + d)i
        return Complex((self.a + other.a), (self.b + other.b))

    def __sub__(self, other):
        # (a + b i) — (c + d i) = (a — c) + (b — d)i
        return Complex((self.a - other.a), (self.b - other.b))

    def __mul__(self, other):
        # (a + b i)(c + di ) = (ac − bd) + (ad + bc)i
        return Complex((self.a * other.a - self.b * other.b), (self.a * other.b + self.b * other.a))


c1 = Complex(2, 3)
c2 = Complex(-1, 1)
print(c1+c2)
print(c1-c2)
print(c1*c2)
print(type(c1+c2))
