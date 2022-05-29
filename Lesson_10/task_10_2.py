# 2. Реализовать проект расчёта суммарного расхода ткани на производство одежды.
# Техническое задание:
#
# +Основная сущность (класс) этого проекта — одежда, которая может иметь определённое название/имя (атрибут).
# +К типам одежды в этом проекте относятся пальто и костюм.
# +У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
# +Это целые числа, например V и H, соответственно. Имена атрибутов можете сделать другими.
# +Создать метод расчета ткани для каждого класса: пальто, костюм по формуле:
# +для пальто '(V/6.5 + 0.5)',
# +для костюма '(2*H + 0.3)'.
# +Выполнить общий подсчёт расхода ткани для всех созданных экземпляров, отдельно для пальто,
# +отдельно для костюма. Алгоритм должен работать для любого кол-ва экземпляров.
# +Общий расход ткани на все экземпляры - это тоже данные. Где их логично хранить?
# +Не принципиально будет ли накапливаться общий расход ткани определенным методом или будет скрыт внутри других методов/конструктора.
# +Проверить на практике полученные на этом уроке знания. Использовать абстрактный класс для «одежды».
# +Подумайте что должно быть абстрактным методом в классе «одежда».
# +Вспомните что должно быть в коде метода, когда он еще не наполнен никакой логикой.
# +Используйте наследование. Переопределите абстрактные методы в классах-наследниках.
# +Проверить работу декоратора '@property'.
# +Не допускайте дублирования кода или спагетти-кода (кода с многочисленными проверками условий).
# +Тщательно продумайте что должно быть данными (атрибутами), а что методами.
# +Создать не менее 3 экземпляров классов с различными данными.
# +Провести расчет ткани для каждого - вывести на экран
# +Продемонстрировать накопительный счетчик общего расхода ткани по каждому классу.

from abc import ABC, abstractmethod


class Clothes(ABC):
    brand = 'Russkiy bogatyr'
    total_quantity = 0  # Накопительный счетчик общего расхода ткани.

    @abstractmethod
    def textile_quantity(self):
        pass


class Coat(Clothes):
    coat_total_quantity = 0  # Накопительный счетчик расхода ткани пальто.

    def __init__(self, V):  # V = size
        self.V = V
        Clothes.total_quantity += self.V/6.5 + 0.5
        Coat.coat_total_quantity += self.V / 6.5 + 0.5

    @property
    def textile_quantity(self):
        print('Coat')
        return self.V/6.5 + 0.5


class Suit(Clothes):
    suit_total_quantity = 0  # Накопительный счетчик расхода ткани костюмов.

    def __init__(self, H):  # H = heigth
        self.H = H
        Clothes.total_quantity += self.H*2 + 0.3
        Suit.suit_total_quantity += self.H*2 + 0.3

    @property
    def textile_quantity(self):
        print('Suit')
        return self.H*2 + 0.3


c1 = Coat(12)
c2 = Coat(1)
c3 = Coat(121)
print(c1.textile_quantity)
print(c2.textile_quantity)
print(c3.textile_quantity)
s1 = Suit(3)
s2 = Suit(7)
print(s1.textile_quantity)
print(s2.textile_quantity)
print('Coat_total_quantity:', Coat.coat_total_quantity)
print('Suit_total_quantity:', Suit.suit_total_quantity)
print('Total_quantity:', Clothes.total_quantity)