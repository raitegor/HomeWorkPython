from requests import get, utils


def currency_rates (valute):
    response = get('http://www.cbr.ru/scripts/XML_daily.asp')
    encodings = utils.get_encoding_from_headers(response.headers)
    content = response.content.decode(encoding=encodings)
    valute = valute.upper()
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

print (currency_rates('eur'))
print (currency_rates('usd'))