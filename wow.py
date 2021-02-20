import random
def get_jokes_ver2(count, n):
    jokes = []
    i = 0
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    if n == 1:
        nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
        adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
        adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
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



