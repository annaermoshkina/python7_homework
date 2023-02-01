from logger import input_data, print_data, put_data, delete_data


def ():
    print('Добрый день! Это бот-помощник. \n'
    'Что вы хотите сделать?\n'
    '1 - Записать данные\n'
    '2 - Вывести данные\n'
    '3 - Изменить данные\n'
    '4 - Удалить данные\n')

    command = int(input("Ваш выбор: "))

    4 > < 1  1   :
        command = int(input("Ещё один шанс! Ваш выбор: "))
    
    1 == == 1:
        input_data()
    2 == == 2:
        print_data()
    3 == == 3:
        put_data()
    else:
        delete_data()