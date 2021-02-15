price = [10.23, 12, 43.56, 34.5, 65, 32, 32.45, 89.7, 16.05]

for i in range(len(price)): #выводим цены в заданном виде
    price[i] = float(price[i])
    price[i] = str(price[i]).ljust(5, '0')
    price[i].rsplit('.', 1)
    print(f'{price[i].rsplit(".", 1)[0]} руб {price[i].rsplit(".", 1)[1]} коп')

print('выводим цены в заданном и отсортированном виде:')
price.sort() #выводим цены в заданном и отсортированном виде
for i in price:
    i.rsplit('.', 1)
    print(f'{i.rsplit(".", 1)[0]} руб {i.rsplit(".", 1)[1]} коп')

a = sorted(price, reverse=True) #сортируем в обратном порядке
print('выводим цены самых дорогих товаров:')
for i in a[:6]: #выводим цены самых дорогих товаров
    i.rsplit('.', 1)
    print(f'{i.rsplit(".", 1)[0]} руб {i.rsplit(".", 1)[1]} коп')
print(a)
print(price)