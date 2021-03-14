import itertools

clients = {}

way_on_people = input('Введи путь к списку людей: ')
way_on_hobby = input('Введи путь к списку хобби: ')

with open(way_on_people + '\\users.csv', 'r', encoding='utf-8') as f:
    persone = (line for line in f)
    with open(way_on_hobby + '\\hobby.csv', 'r', encoding='utf-8') as b:
        hobby = (line for line in b)
        for i in itertools.zip_longest(persone, hobby):
            if i[1] != None:
                clients[i[0][:-1]] = i[1][:-1]
            else:
                clients[i[0][:-1]] = i[1]
way_to_save = input('Введи путь куда хохранить общий список: ')
with open(way_to_save + '\\clients.csv', 'w', encoding='utf-8') as f:
    for i in clients.items():
        f.write(str(i) + '\n')