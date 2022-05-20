import datetime

x = datetime.datetime.now()
num_day_year = (x.strftime("%j"))
open_reading_file = open('holiday', encoding='utf-8').read().split('\n')[int(num_day_year)]
print(open_reading_file)
if 'нет' not in open_reading_file:
    while True:
        question = input('Хотите узнать больше об этом празднике? (да/нет): ')
        if question == 'нет':
            print('Программа завершена.')
            break
        elif question == 'да':
            x2 = datetime.datetime.now()
            num_day_year2 = (x2.strftime("%d"))
            open_reading_file2 = open('information', encoding='utf-8').read().split('\n')[int(num_day_year2)]
            print(open_reading_file2)
            break
        else:
            print('Некорректный ввод, попробуйте снова.')
            continue
