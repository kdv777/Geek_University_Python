# 1. Написать функцию 'email_parse(<email_address>)', которая при помощи
# регулярного выражения извлекает имя пользователя и почтовый домен из email адреса
# и возвращает их в виде словаря.

import re

mail_regexp = "(?P<username>[a-zA-Z0-9\_\.'+-]+)@(?P<domain>([a-zA-Z0-9\.-]+\.{1}[a-zA-Z0-9\.-]+))"


def email_parse(email):
    result = re.match(mail_regexp, email)
    if not result:
        raise ValueError(f'wrong email: {email}')
    return result.groupdict()


with open('task_8_1_test_email2.txt', mode='r', encoding='utf-8') as f:
    for line in f:
        try:
            print(f'{line.strip()}{email_parse(line)}')
        except ValueError:
            print(f"{line.strip()}  Error")

# print(email_parse('someone@geekbrains.ru'))
# print(email_parse('some1_one.two+three@geekbrains7.ru.net'))
# print(email_parse('someone@geekbrainsru'))
# print(email_parse('user5=name@domenname.ru'))

# для парсинга файла с email
# RE_MAILS = re.compile(r"(?P<username>[\w+.\-'_]+)@{1}(?P<domain>[\w+\-]+\.[\w+\-\.]+)")
# print(*map(lambda x: x.groupdict(), RE_MAILS.finditer('someone@geekbrains.ru')), sep=', ')
# print(*map(lambda x: x.groupdict(), RE_MAILS.finditer('someone@geekbrainsru')), sep=', ')
# print(*map(lambda x: x.groupdict(), RE_MAILS.finditer('sdkfjhks_123+3HJGJ@test.domian1.ru')), sep=', ')
