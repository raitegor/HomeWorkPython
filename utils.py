from requests import get, utils
import datetime

def currency_rates (valute):
    response = get('http://www.cbr.ru/scripts/XML_daily.asp')
    encodings = utils.get_encoding_from_headers(response.headers)
    content = response.content.decode(encoding=encodings)
    valute = valute.upper()
    data = content.split('Date="')
    data = data[1][:10].split('.')
    data = datetime.date(int(data[2]), int(data[1]), int(data[0]))
    print(data)
    if valute in content and len(valute)==3:
        a=content.split('</Valute>')
        b = None
        for i in a:
            if valute in i:
                b = i
        end = b.find('</Value>')
        start = end - 7
        b = float(b[start:end].replace(',', '.'))
        return b
    else:
        return None