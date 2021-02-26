import itertools

number = 21
gen = (num for num in range(1, number + 1, 2))
print(*itertools.islice(gen, 4))