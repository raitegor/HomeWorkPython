number = int(input('Введите число: '))
list_2 = [ 2, 3, 4]
list_3 = [ 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
if number == 1:
    print(number, 'Процент')
elif number in list_2:
    print(number, 'процента')
elif number in list_3:
    print(number, 'процентов')
