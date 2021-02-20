
my_dict = {}

def thesaurus(*name):
    name = list(name)
    for i in name:
        if i[:1] in my_dict:
            my_dict[i[:1]].append(i)
        else:
            my_dict.setdefault(i[:1], [i])

thesaurus('Валера', 'Антон', 'Кира', 'Витя')


print(my_dict)
