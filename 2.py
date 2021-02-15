import copy
first_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']


for i in first_list[:]:
    if i.isdigit():
        first_list.insert(first_list.index(i), '"')
        first_list.insert(first_list.index(i)+1, '"')
        first_list[first_list.index(i)] = first_list[first_list.index(i)].zfill(2)
    elif i[0] == '+':
        first_list.insert(first_list.index(i), '"')
        first_list.insert(first_list.index(i) + 1, '"')
        first_list[first_list.index(i)] = first_list[first_list.index(i)].zfill(3)
first_list = ' '.join(first_list)

print(first_list)





