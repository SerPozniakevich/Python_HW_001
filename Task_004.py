# Напишите программу, которая по заданному номеру четверти, 
# показывает диапазон возможных координат точек в этой четверти (x и y).

its_quarter = int(input('Введите номер четверти: '))

if(its_quarter == 1):
    print('X > 0; Y > 0;')
if(its_quarter == 2):
    print('X < 0; Y > 0;')
if(its_quarter == 3):
    print('X < 0; Y < 0;')
if(its_quarter == 4):
    print('X > 0; Y < 0;')
if(its_quarter < 1 or its_quarter > 4):
    print('Введена неправильная четверть')
