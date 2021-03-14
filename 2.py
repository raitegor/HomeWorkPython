ip = {}
with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
    black_list = (line.split(' ')[0]for line in f)
    for i in black_list:
        if i in ip:
            ip[i] +=1
        else:
            ip[i] = 1

max_count = max(ip.values())
print(max_count)
for k, v in ip.items():
    if v == max_count:
        print(k)

#ip = []
# a = 0
# b = None
# for i in ip:
#     if a < ip.count(i):
#         a = ip.count(i)
#         b = i
# print(a, b)

