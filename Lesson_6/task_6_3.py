# 3. Есть два файла: в одном хранятся ФИО пользователей сайта, а в другом — данные об их хобби.
# Загрузить данные из обоих файлов и сформировать словарь: ключи — ФИО, значения — данные о хобби.
# Сохранить словарь в текстовый файл. Проверить сохранённые данные.

result = {}
with open('users.csv', 'r') as f_users, open('hobby.csv', 'r') as f_hobby:
    for line in f_users:
        users_str = line.strip()
        # Составляем список ФИО
        users_list = users_str.split(',')
        # Взять первые только первые буквы ФИО.
        users_str = users_list[0][0] + users_list[1][0] + users_list[2][0]
        hobbys_str = f_hobby.readline().replace('\n', '').replace(',', ';')
        if not hobbys_str:
            hobbys_str = None
        result[users_str] = hobbys_str

    if f_hobby.readline():
        print(result)
        print('Error code №1')
    else:
        print(result)

    # Записываем результат в текстовый файл
    with open('result.txt', 'w', encoding='utf-8') as f:
        f.write(str(result))
