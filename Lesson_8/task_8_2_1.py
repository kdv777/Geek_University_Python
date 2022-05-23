# 2. Усложнение:
#
# Ваша функция должна корректно обрабатывать как IPv4, так и IPv6 - найдите их в лог-файле.
# Посмотрите спецификацию IPv6. Что такое шестнадцатеричное число и какие буквы/цифры оно может включать.
# Сколько их может быть в IPv6.
# Совсем хорошо, если вы обработаете cокращенные адреса IPv6, которые тоже в есть в лог файле.
# Ваш шаблон должен пропускать только то, что нужно, не используйте «избыточно широкие» шаблоны.


import re

RE_DATE = re.compile(r'(?P<remote_addr>(^(\d{1,3}\.){3}\d{1,3})|([\w\d\:]){2,39})(\s-\s-\s)'
                     r'(\[(?P<request_datetime>(\d{1,2}\/\w+\/\d{4}(:\d{2}){3}\s\+\d{4}))])\s'
                     r'(\"(?P<request_type>\w+)(\s))((?P<request_resource>(\/\w+)*))(\s*\w*...."\s'
                     r'(?P<response_code>\d*)\s(?P<response_size>\d*))')


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
