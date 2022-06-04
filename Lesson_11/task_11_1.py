from datetime import date


class DateInitError(Exception):
    def __str__(self):
        return 'Ошибка, невозможно создать объект!'


class Data:
    def __init__(self, my_date):
        try:
            day, month, year = self.data_int(my_date)
            if self.valid_date(year, month, day):
                self.day = day
                self.month = month
                self.year = year
            else:
                raise DateInitError
        except DateInitError as err:
            print(err)

    def __str__(self):
        # Переопределить метод 'str' для печати числа в виде '2021.12.31'
        try:
            result = f'{self.year}.{self.month}.{self.day}'
        except (AttributeError, TypeError):
            return ''
        else:
            return result

    @classmethod
    def data_int(cls, str_date):
        # Извлекает число, месяц, год из строки «день-месяц-год», преобразовывает их к типу 'int'.
        # Возвращает три числа, если не получилось - выкидывает исключение (тип исключения на ваш выбор)
        # str_date = "31-12-2022"
        try:
            day, month, year = map(int, str_date.split("-"))
        except ValueError:
            raise DateInitError
        else:
            return day, month, year

    @staticmethod
    def valid_date(year, month, day):
        # Проводит валидацию этих трех чисел, например, месяц — от 1 до 12, дней в месяце не более 31 -
        # далее на ваш выбор. Вы можете использовать пакет datetime для проверки корректности даты.
        # Возвращает True или False. Могут ли здесь возникнуть исключения?
        try:
            if date(year, month, day):
                return True
        except ValueError:
            return False


d1 = Data("31-12-2022")
print(d1)
d2 = Data("aa-12-2022")
print(d2)
d3 = Data("32-12-2022")
print(d3)
d4 = Data("31--01-2021")
print(d4)
