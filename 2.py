numbers = []
all_sum = 0
for number in range (1, 1000, 2):
    numbers.append(number**3)
print(numbers)
for number in numbers:
    suma = 0
    a = number + 17
    while a > 0:
        last = a % 10
        suma = suma + last
        a = a // 10
    if suma % 7 == 0:
        all_sum = all_sum + number
print(all_sum)





