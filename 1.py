def odd_nums(numbers):
    for number in range(1, numbers + 1, 2 ):
        yield number

add_to = odd_nums(15)

print(next(add_to),next(add_to), next(add_to))