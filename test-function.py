#price = 100
#vat_rate = 18
#vat = price / 100 * vat_rate
#print(vat)

def get_vat(price, vat_rate):
    try:
        price = float(price)
        vat_rate = float(vat_rate)
        vat = price / 100 * vat_rate
        price_no_vat = price - vat
        price_no_vat = round(price_no_vat,2)
        return 'Цена без НДС: {}'.format(price_no_vat)
    except (TypeError, ValueError):
        return 'Не могу сделать расчет. Проверьте вводимые данные.'



price1 = 'ololo'
vat1 = '12'
result = get_vat(price1, vat1)
print(result)