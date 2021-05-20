import requests
import json
import time

#to change how often data is updated change this variable
update_interval_sec = 3600

cryptos = [
	"monero",
	"iota",
	"tezos",
	"bitcoin-cash-sv",
	"cosmos",
	"bittorrent-2",
	"dash",
	"zcash",
	"bitcoin",
	"ethereum",
	"binancecoin",
	"cardano",
	"dogecoin",
	"ripple",
	"bitcoin-cash",
	"exchange-union",
	"litecoin",
	"chainlink",
	"stellar",
	"vechain",
	"ethereum-classic",
	"theta-token",
	"tron",
	"eos",
	"filecoin",
	"terra-luna"
	,"neo"
	]

header_str = '%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s' % (
	'local_machine_time',
	'last_updated',
	'id',
	'name',
	'symbol',
	'rank',
	'price_usd',
	'24h_volume_usd',
	'market_cap_usd',
	'available_supply',
	'total_supply',
	'percent_change_1h',
	'percent_change_24h',
	'percent_change_7d'
	)

print(header_str) # will need to remove once you are done 

while  1==1:
	for i in range(0,len(cryptos)):
		link = "https://api.alternative.me/v1/ticker/%s/" % cryptos[i]
		cryto_json = json.loads(requests.get(link).text.replace('[','').replace(']',''))
		crypto_str = '%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s' % (
			time.time(),
			cryto_json['last_updated'],
			cryto_json['id'],
			cryto_json['name'],
			cryto_json['symbol'],
			cryto_json['rank'],
			cryto_json['price_usd'],
			cryto_json['24h_volume_usd'],
			cryto_json['market_cap_usd'],
			cryto_json['available_supply'],
			cryto_json['total_supply'],
			cryto_json['percent_change_1h'],
			cryto_json['percent_change_24h'],
			cryto_json['percent_change_7d']
			)
		print(crypto_str)
	time.sleep(update_interval_sec)


# print(cryto_json)