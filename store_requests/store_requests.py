import requests


class store():
	def __init__(self, store_name, api_key, params, relevant_info, url):
		self.name    = store_name
		self.api_key = api_key
		self.keys    = relevant_info 
		self.url     = url
		self.params  = params

	def get_json(self, id):
		req_url = self.url + '?' + '&'.join([self.params['api_key'], self.params['get_item'] + '=' + str(id) ])
		
		r = requests.request('GET', req_url ).json()['items'][0]

		ret = {k : r[k] for k in self.keys}
		return ret
 




api_keys = {
	'walmart': 's6md6cnzakj5cgw38tsavu7s'
}

stores = {
	'walmart': store(store_name= 'walmart', 
		api_key=api_keys['walmart'], 
		relevant_info=['msrp', 'largeImage'], 
		url='http://api.walmartlabs.com/v1/items',
		params={
			'api_key': 'apiKey=' + api_keys['walmart'],
			'get_item': 'upc'
		}),
	}



def get_json(store, id='035000521019'):
	return stores[store].get_json(id)
