
numero = []
with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
    black_list = ((line.split(' ')[0], line.split(' ')[5][1:], line.split(' ')[6]) for line in f)
    for i in black_list:
        numero.append(i)
print(numero)





