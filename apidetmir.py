import json
import requests
import csv

baby_items = {
		'podguzniki': 'Подгузники',
	 	'diapers_pants': 'Подгузники-трусики',
	 	'pure' : 'Пюре', 
		'chai': 'Чай детский', 
		'fruchtgetranke' : 'Соки, воды, компоты, морсы' , 
		'grocery': 'Бакалея', 
		'kashi': 'Каши', 
		'suhie_smesi_i_zameniteli_moloka': 'Смеси и заменители молока'
		}

def write_csv(data, category):
	with open(f'{baby_items[category]}.csv', 'a', encoding='utf-8') as f:
	#w write data
	#a append data
		writer = csv.writer(f)
		writer.writerow((data['name'],
						 data['price'],
						 data['currency']))
def get_data(category):
	url =f'https://api.detmir.ru/v2/products?filter=categories[].alias:{category};withregion:RU-BA'
	parameters = {'meta': 'long', 'limit': '1'}
	r = requests.get(url, params = parameters)
	length = r.json()['meta']['length']
	new_parameters = {'limit': length}
	items = requests.get(url, params = new_parameters).json()
	for item in items:
		name = item['title']
		try:
			price = item['price']['price'] 
		except KeyError: 
			price = ''
		try:
			currency = item['price']['currency']
		except KeyError:
			currency = ''
		data={'name': name, 'price': price, 'currency': currency}
		write_csv(data, category)
	print(f'Данные категории {baby_items[category]} собраны')




def main():
	for category in baby_items:
		get_data(category)
	print('Готово')



if __name__ == '__main__':
	main()

