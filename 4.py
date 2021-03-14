import itertools

clients = {}


with open('users.csv', 'r', encoding='utf-8') as f:
    persone = (line for line in f)
    with open('hobby.csv', 'r', encoding='utf-8') as b:
        hobby = (line for line in b)
        for i in itertools.zip_longest(persone, hobby):
            if i[1] != None:
                clients[i[0][:-1]] = i[1][:-1]
            else:
                clients[i[0][:-1]] = i[1]



print(clients)