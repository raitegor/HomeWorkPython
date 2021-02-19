
def thesaurs_adv(*name):
    my_dict = {}
    name = list(name)
    for i in name:
        n, sern = i.split()
        di = my_dict.get(sern[0])
        if di is None:
            di = {}
        st = di.get(n[0])
        if st is None:
            st = []
        st.append(i)
        di.setdefault(n[0], st)
        my_dict.setdefault(sern[0], di)

    my_dict_sort = {}
    for i in sorted(my_dict.keys()):
        my_dict_sort.setdefault(i, my_dict[i])
    return my_dict_sort

print(thesaurs_adv('Егор Райт', 'Ваня Егоров', 'Валеря Ермак', 'Оксана Петрушкина', 'Ереван Ромов', 'Ермак Колесов', 'Валера Рабин'))



