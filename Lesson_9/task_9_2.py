# 2. Реализовать класс Road (дорога).
# Техническое задание:
#
# определить атрибуты: length (длина), width (ширина). Подумайте атрибуты чего?
# значения атрибутов должны передаваться при создании экземпляра класса
# атрибуты сделать защищёнными
# определить метод расчёта массы асфальта, необходимого для покрытия всей дороги
# метод возвращает массу асфальта в виде строки в требуемом формате (см примеры/тесты)
# формула 'длина * ширина * масса асфальта для покрытия одного кв. метра дороги асфальтом, ' \
#         'толщиной в 1 см * число см толщины полотна';
# проверить работу метода и вывести массу асфальта для 2-3 наборов параметров.

class Road:

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calc_mass(self):
        mass = f'{int(self._length * self._width * 25 * 5 / 1000)} т'
        return mass


a = Road(20, 5000)
print(a.calc_mass())
a2 = Road(40, 3000)
print(a2.calc_mass())
a3 = Road(77, 8000)
print(a3.calc_mass())