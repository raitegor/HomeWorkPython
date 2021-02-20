
def num_translate( number ):
    num = {
        'one': 'один',
        'two': 'два',
        'three': 'три',
        'four': 'четыре',
        'five': 'пять',
        'six': 'шесть',
        'seven': 'семь',
        'eight': 'восемь',
        'nine': ' девять',
        'ten': 'десять'
    }
    if number.istitle():
        number = number.lower()
        return num.get(number).capitalize()
    else:
        return num.get(number)

a = input('Type a number: ')
print(num_translate(a))


