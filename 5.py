
import random

""" Функция которая генерирует случайные шутки"""

def get_jokes(count):
    jokes = []
    i = 0
    while i < count:
        nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
        adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
        adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
        words = random.randint(0, len(nouns)-1)
        joke = nouns[words] +' '+ adverbs[words] +' '+ adjectives[words]
        i+=1
        jokes.append(joke)

    return jokes

""" Функция которая генерирует шутки и запрещает или разрешает повтор слов в шутках
если n = 1 то слова не повторяются. """
def get_jokes_ver2(count, n):
    jokes = []
    i = 0
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    if n == 1:
        while i < count:
            words = random.randint(0, len(nouns)-1)
            joke = nouns.pop(words) +' '+ adverbs.pop(words) +' '+ adjectives.pop(words)
            i+=1
            jokes.append(joke)
        return jokes
    else:
        while i < count:
            words = random.randint(0, len(nouns) - 1)
            joke = nouns[words] + ' ' + adverbs[words] + ' ' + adjectives[words]
            i += 1
            jokes.append(joke)

        return jokes