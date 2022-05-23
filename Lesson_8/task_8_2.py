# 2. [Задача со звездочкой]: усложненный вариант задания 1. Написать регулярное выражение для парсинга файла логов web-сервера из ДЗ 6 урока nginx_logs.txt
# Техническое задание:
#
# Лог файл: https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs
# Функция парсинга строки лог-файла:
# Принимает параметр: строка для пасинга, при необходимости и другие параметры
# возвращает кортеж из 6 элементов вида: ('<remote_addr>, <request_datetime>, <request_type>, <requested_resource>, '
#                                         '<response_code>, <response_size>)'
# Вы можете не обращать внимание на IPv6 или явно учесть их в регулярном выражении, это будет очень хорошо.
# Проверьте работоспособность функции на нескольких строках лог файла.
# Распарсите весь файл и сформируйте список всех IP лог файла, без повторений. Выведите в консоль его длину.

# +1. написать RegExp
# 2. +открыть файл
# 3. +сформировать кортеж
# 4. +сформируйте список всех IP лог файла, без повторений. Выведите в консоль его длину.

import re

RE_DATE = re.compile(r'(?P<remote_addr>(^(\d{1,3}\.){3}\d{1,3})).*(\[(?P<request_datetime>'
                     r'(\d{1,2}\/\w+\/\d{4}(:\d{2}){3}\s\+\d{4}))])\s("(?P<request_type>\w+)(\s))'
                     r'((?P<request_resource>(\/\w+)*))(\s*\w*...."\s(?P<response_code>\d*)\s'
                     r'(?P<response_size>\d*))')


def pars_log(argum):
    result = RE_DATE.match(argum)
    if result:
        return result.groupdict()
    else:
        return None


result_ip = []
with open('nginx_logs.txt', mode='r', encoding='utf-8') as f:
    for line in f:
        if pars_log(line):
            pars_res = pars_log(line)
            # Формируем список всех IP лог файла, без повторений.
            if pars_res['remote_addr'] not in result_ip:
                result_ip.append(pars_res['remote_addr'])
    len_list = len(result_ip)

# print(*result_ip, sep='\n')
print('Длина списка = ', len_list)
