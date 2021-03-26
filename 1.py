import re

text = 'Мой емаил очень не обычный renge@mail.ru вот такой вот он'

my_dict ={}
RE_Name = re.compile (r'([\w]+)@\s*')
RE_Name_1 = re.compile (r'\@([\w]+[.]+[\w]+)')
my_dict['username'] = RE_Name.findall(text)[0]
my_dict['domain'] = RE_Name_1.findall(text)[0]

print (my_dict)

