import json
from pprint import pprint

with open('prices.json') as data_file:
	data = json.load(data_file)

sumPrices = 0
for price in data:
	sumPrices += int(price['price'][1:].replace(',',''))

avgPrice = sumPrices/len(data)

print avgPrice