# 3. Написать декоратор для логирования(вывод в консоль) типов позиционных аргументов функции:
# Техническое задание:
#
# Если аргументов несколько - выводить данные о каждом через запятую.
# Все выводы должны быть внутри функции-обертки/задекорированной функции
# После того как вы «обернули»/«задекорировали» функцию убедитесь что и аргументы,
# и возвращаемое значение остались как у исходной функции. Т.е. вызов задекорированной функции
# ничем не отличается от вызова исходной функции, результат возвращается такой же, но добавляется печать в консоль.

# Усложнение:
#
# + вывести тип возвращаемого значения функции
# + решить задачу для именованных аргументов
# + вывести имя функции


# def old_func(*args, **kwargs):
#     return 1


def type_logger(func):
    def _wrapper(*args, **kwargs):
        result = func(*args, **kwargs)

        print('Вывод аргументов функции old_func:')
        for el in args:
            print(f'{el}: {type(el)}', ', ', end=' ')
        for el2 in kwargs:
            print(f'{el2}: {type(el2)}', ', ', end=' ')

        print('\n', '-----------------')
        print(f'Тип возвращаемого значения функции: {type(func())}')
        print(f'Имя функции: {func.__name__}')

        return result
    return _wrapper


@type_logger
def old_func(*args, **kwargs):
    return 1


old_func(1, 2.0, 'word', True, a='Именованный аргумент')
