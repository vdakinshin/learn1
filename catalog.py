catalog_item = {
    'type': 'phone',
    'vendor': 'Apple',
    'model': 'iphone 7 black',
    'price': 37.5
}

catalog_item['audio_jack'] = False
catalog_item['price'] = 70

#item_name = catalog_item['vendor'] + ' ' + catalog_item['model']

#item_name = catalog_item.get('vendor') + ' ' + catalog_item.get('model')

#catalog_item['discount']
#print(catalog_item['discount'])

#print(catalog_item.get('discount', 'Скидок не будет!!'))

#a = 'model' in catalog_item
#print('Ключ model есть в каталоге? {}' .format(a))

#b = 'discount' not in catalog_item
#print('Ключа discount нет в каталоге? {}' .format(b))

#c = 'discount' in catalog_item
#print('Ключ discount есть в каталоге? {}' .format(c))

#for key in catalog_item:
#    print(key)

#for key, value in catalog_item.items():
#    print('{}: {}' . format(key, value))

print(catalog_item)

try:
    del catalog_item['discount']
except KeyError:
    pass

print(catalog_item)
