time = int(input('Введите количество сек: '))

hours = time//3600
min = (time % 3600) // 60
sec = ((time % 3600) % 60)
print(hours, 'час/', min, 'мин/', sec, 'сeк/', sep=' ')