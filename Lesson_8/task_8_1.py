# 1. Написать функцию 'email_parse(<email_address>)', которая при помощи
# регулярного выражения извлекает имя пользователя и почтовый домен из email адреса
# и возвращает их в виде словаря.

import re


def email_parse(email):
    result = re.match(r"(?P<username>[\w+.\-'_]+)@{1}(?P<domain>[\w+\-]+\.[\w+\-\.]+)", email)
    if not result:
        msg = f'wrong email: {email}'
        raise ValueError(msg)
    return result.groupdict()


print(email_parse('someone@geekbrains.ru'))
print(email_parse('some1_one.two+three@geekbrains7.ru.net'))
print(email_parse('someone@geekbrainsru'))

# для парсинга файла с email
# RE_MAILS = re.compile(r"(?P<username>[\w+.\-'_]+)@{1}(?P<domain>[\w+\-]+\.[\w+\-\.]+)")
# print(*map(lambda x: x.groupdict(), RE_MAILS.finditer('someone@geekbrains.ru')), sep=', ')
# print(*map(lambda x: x.groupdict(), RE_MAILS.finditer('someone@geekbrainsru')), sep=', ')
# print(*map(lambda x: x.groupdict(), RE_MAILS.finditer('sdkfjhks_123+3HJGJ@test.domian1.ru')), sep=', ')
