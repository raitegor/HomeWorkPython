import itertools

clients = {}
peoples = []
hobbys = []


with open('users.csv', 'r', encoding='utf-8') as f:
    persone = (line for line in f)
    for i in persone:
        peoples.append(i[:-1])

with open('hobby.csv', 'r', encoding='utf-8') as b:
    hobby = (line for line in b)
    for i in hobby:
        hobbys.append(i[:-1])


for i in itertools.zip_longest(peoples, hobbys):
    clients[i[0]] = i[1]

print(clients)
