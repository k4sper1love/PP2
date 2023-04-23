import psycopg2, csv, time
from config import config
import functions

# if __name__ == '__main__':
#     functions.create_tables()
status = True
while True:
    print('''Хотите начать/продолжить работу с БД phonebook? 1. Далее // 2. Выход''')
    choice_work = int(input('Выберите цифру: '))
    if choice_work != 1: quit()
    print('''
Пожалуйста, выберите способ работы с phonebook.
    1. Загрузка данных из csv-файла
    2. Ввод данных с консоли
    3. Изменить данные
    4. Запросить данные из таблицы 
    5. Удалить данные из таблицы
    6. Выход''')
    choice = int(input('Введите цифру: '))
    if choice == 1:
        name_csv = input("Введите имя CSV файла без расширения: ")
        id_list = functions.add_data_from_csv(name_csv)

    elif choice == 2:
        choice_vvod = int(input('Выберите: 1. Добавить 1 пользователя, 2. Добавить множество пользователей..... Цифра: '))
        if choice_vvod == 1:
            new_user_name = str(input("Введите имя пользователя: "))
            new_user_phone = str(input('Введите номер телефона в любом формате: '))
            new_user_id = functions.add_data_from_console(new_user_name, new_user_phone)
        elif choice_vvod == 2:
            choice_vvod_method = int(input('Выберите: 1. Перечислить по отдельности, 2. Взять данные из списка..... Цифра: '))
            if choice_vvod_method == 1:
                error_id = []
                count_vvod = int(input('Сколько пользователей вы хотите добавить? '))
                for x in range(0, count_vvod):
                    new_user_name = str(input("Введите имя пользователя: "))
                    new_user_phone = str(input('Введите номер телефона в любом формате: '))
                    if functions.check_data(new_user_phone):
                        new_user_id = functions.add_data_from_console(new_user_name, new_user_phone)
                    else:
                        print('Пользователь с номером {0} уже добавлен.'.format(new_user_phone, ))
            elif choice_vvod_method == 2:
                path_vvod = str(input('Введите имя файла .txt, где список(имя,телефон): '))
                with open('LAB11/phonebook/{0}.txt'.format(path_vvod), 'r', encoding='utf-8') as file:
                    content = file.read()
                    list_vvod = content.split(',')
                if len(list_vvod) % 2 != 0:
                    print('Неправильно введен список. Не у всех элементов имя, телефон есть пара.')
                else:
                    number_vvod = 0
                    for x in range(0, len(list_vvod)// 2):
                        new_user_name = str(list_vvod[number_vvod])
                        new_user_phone = str(list_vvod[number_vvod + 1])
                        number_vvod += 2
                        if functions.check_data(new_user_phone):
                            new_user_id = functions.add_data_from_console(new_user_name, new_user_phone)
                        else:
                            print('Пользователь с номером {0} уже добавлен.'.format(new_user_phone, ))
            



    elif choice == 3:
        print('''Выберите метод: 
    1. По id пользователя
    2. По номеру телефона
    3. Назад''')
        choice_update = int(input("Введите цифру: "))
        if choice_update == 1:
            user_id = int(input('Введите id пользователя: '))
            print('''Выберите цель:
    1. Обновить имя пользователя
    2. Обновить номер телефона
    3. Назад''')
            choice_update_second = int(input('Введите цифру: '))
            if choice_update_second == 1:
                new_name = str(input('Введите новое имя пользователя: '))
                functions.update_name(user_id, new_name, 1, 1)
                print('Данные успешно обновлены.')
            elif choice_update_second == 2:
                new_phone = str(input('Введите новый номер телефона: '))
                functions.update_name(user_id, new_phone, 1, 2)
                print('Данные успешно обновлены.')
        elif choice_update == 2:
            user_phone = str(input('Введите номер телефона: '))
            print('''Выберите цель:
    1. Обновить имя пользователя
    2. Обновить номер телефона
    3. Назад''')
            choice_update_second = int(input('Введите цифру: '))
            if choice_update_second == 1:
                new_name = str(input('Введите новое имя пользователя: '))
                functions.update_name(user_phone, new_name, 2, 1)
                print('Данные успешно обновлены.')
            elif choice_update_second == 2:
                new_phone = str(input('Введите новый номер телефона: '))
                functions.update_name(user_phone, new_phone, 2, 2)
                print('Данные успешно обновлены.')
    elif choice == 4:
        print('''Выберите формат запроса:
    1. Единичная строка (по id или номеру) / Несколько строк
    2. Полная таблица
    3. Список всех id/Имен/Номеров
    4. Назад''')
        choice_query = int(input('Введите цифру: '))
        if choice_query == 1:
            print('''Найти по:
    1. ID
    2. Номер телефона
    3. Имя (Возможно несколько строк, сортировка по id)
    4. Назад''')
            choice_query_find = int(input('Введите цифру: '))
            if choice_query_find == 1:
                user_id = int(input('Введите id: '))
                rows, count_rows =functions.get_data(user_id, 1, 1)
                print('Найдено строк: {0}'.format(count_rows))
                functions.data_page(rows, 1, 1)
            elif choice_query_find == 2:
                user_phone = str(input('Введите номер телефона: '))
                rows, count_rows = functions.get_data(user_phone, 1, 2)
                print('Найдено строк: {0}'.format(count_rows))
                functions.data_page(rows, 1, 2)
            elif choice_query_find == 3:
                user_name = str(input('Введите имя: '))
                rows, count_rows = functions.get_data(user_name, 1, 3)    
                if count_rows > 5:    
                    page_count = int(input('Найдено строк: {0}. Введите кол-во элементов на странице: '.format(count_rows)))
                else:
                    print('Найдено строк: {0}'.format(count_rows))
                    page_count = 5
                functions.data_page(rows, 1, 3, page_count)   
        elif choice_query == 2:
            print('''Выберите метод сортировки:
    1. По id
    2. По имени пользователя
    3. По номеру телефона
    4. Назад''')
            choice_query_sort = int(input('Введите цифру: '))
            if choice_query_sort == 1:
                rows, count_rows = functions.get_data(None, 2, None)
                page_count = int(input('Найдено строк: {0}. Введите кол-во элементов на странице: '.format(count_rows)))
                functions.data_page(rows, 2, None, page_count)
            elif choice_query_sort == 2:
                rows, count_rows = functions.get_data(None, 2, None, 'user_name')
                page_count = int(input('Найдено строк: {0}. Введите кол-во элементов на странице: '.format(count_rows)))
                functions.data_page(rows, 2, None, page_count)
            elif choice_query_sort == 3:
                rows, count_rows = functions.get_data(None, 2, None, 'user_phone')
                page_count = int(input('Найдено строк: {0}. Введите кол-во элементов на странице: '.format(count_rows)))
                functions.data_page(rows, 2, None, page_count)
        elif choice_query == 3:
            print('''Какой список вы хотите получить?
    1. ID
    2. Имена
    3. Номера телефонов''')
            choice_query_list = int(input('Введите цифру: '))
            if choice_query_list == 1:
                rows,count_rows = functions.get_data(None, 3, 1)
                page_count = int(input('Найдено строк: {0}. Введите кол-во элементов на странице: '.format(count_rows)))
                functions.data_page(rows, 3, 1, page_count)
            elif choice_query_list == 2:
                rows, count_rows = functions.get_data(None, 3, 2)
                page_count = int(input('Найдено строк: {0}. Введите кол-во элементов на странице: '.format(count_rows)))
                functions.data_page(rows, 3, 1, page_count)
            elif choice_query_list == 3:
                rows, count_rows = functions.get_data(None, 3, 3)
                page_count = int(input('Найдено строк: {0}. Введите кол-во элементов на странице: '.format(count_rows)))
                functions.data_page(rows, 3, 1, page_count)
    elif choice == 5:
        print('''Какие вы хотите удалить данные?
    1. Частично
    2. Полностью''')
        choice_delete = int(input('Введите цифру: '))
        if choice_delete == 1:
            print('''Как вы хотите удалить данные из таблицы?
    1. По ID
    2. По номеру
    3. По имени''')
            choice_delete_method = int(input('Введите цифру: '))
            if choice_delete_method == 1:
                user_id = str(input('Введите id: '))
                functions.delete_data(user_id, 1)
            elif choice_delete_method == 2:
                user_phone = str(input('Введите номер телефона: '))
                functions.delete_data(user_phone, 2)
            elif choice_delete_method == 3:
                user_name = str(input('Введите имя: '))
                functions.delete_data(user_name, 3)
        elif choice_delete == 2:
            functions.delete_data(None, 4)
    elif choice == 6:
        quit()
    time.sleep(1)
    