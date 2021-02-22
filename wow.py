import datetime
from requests import get, utils
n = datetime.datetime.now()
print(n)

response = get('http://www.cbr.ru/scripts/XML_daily.asp')
encodings = utils.get_encoding_from_headers(response.headers)
content = response.content.decode(encoding=encodings)
print(content)

a = content.split('Date="')
a = a[1][:10].split('.')
a=datetime.date(int(a[2]), int(a[1]), int(a[0]))
print(a)