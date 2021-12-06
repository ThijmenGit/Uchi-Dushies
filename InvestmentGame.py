import requests
import datetime

class APIRequest:
    def __init__(self):
        return

    def getstockmetadata(self):
        query = input("What would you like: ")

        url = (f'https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords={query}&apikey=73R6EIWTFXMUJFO0')
        r = requests.get(url)
        data = r.json()

        counter = 0
        for item in data['bestMatches']:
            counter += 1
            print(f"Option {counter}: \n \t Company name is: {item['2. name']} \n \t Tracker is: {item['1. symbol']} \n \t Region is: {item['4. region']} \n \t Currency is: {item['8. currency']}")



        option = int(input("Enter the symbol of the Stock you want to buy: "))
        stockmetadata = (data['bestMatches'][option-1])
        return stockmetadata

    def getcurrentvalue(self, stockname):
        df = []
        tracker = stockname['1. symbol']
        url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={tracker}&outputsize=full&apikey=73R6EIWTFXMUJFO0"
        response = requests.get(url)
        if response.status_code != 200:
            raise ValueError("Could not retrieve data, code:", response.status_code)
        raw_data = response.json()
        df.append(raw_data['Time Series (Daily)'][datetime.date.today().strftime('%Y-%d-%m')])
        return(df[0])

    def getspecificvalue(self, stockdate, stockname):
        df = []
        tracker = stockname['1. symbol']
        response = requests.get(f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={tracker}&outputsize=full&apikey=73R6EIWTFXMUJFO0")
        if response.status_code != 200:
            raise ValueError("Could not retrieve data, code:", response.status_code)
        raw_data = response.json()
        df.append(raw_data['Time Series (Daily)'][stockdate])
        return(df[0])
        #fix stockdate

    def stockpackage(self, stockmetadata, stockprice):
        stock = {'Tracker': 'KPN.AMS', 'Name': 'Koninklijke KPN N.V.', 'Region': 'Amsterdam', 'Currency': 'Eur',
                 'Lastprice': '2.78'}
        dict1 = stockmetadata
        dict2 = stockprice
        dict3 = dict(dict1, **dict2)

        keys_to_remove = ['3. type', '5. marketOpen', '6. marketClose', '7. timezone', '9. matchScore', '1. open', '2. high', '3. low', '5. volume']
        for keys in keys_to_remove:
            dict3.pop(keys)

        old_key = ['1. symbol', '2. name', '4. region', '8. currency', '4. close']
        new_key = ['Tracker', 'Name', 'Region', 'Currency', 'Buyingprice']
        count = 0
        for items in old_key:
            dict3[new_key[count]] = dict3.pop(old_key[count])
            count += 1
        return dict3

if __name__=="__main__":
    API = APIRequest()
    stockmetadata = API.getstockmetadata()
    stockprice = API.getcurrentvalue(stockmetadata)
    #df = API.getspecificvalue('2020-01-01', stockmetadata)
    stockpackage = API.stockpackage(stockmetadata, stockprice)
    print(stockpackage)

# Since we are retrieving stuff from a web service, it's a good idea to check for the return status code
# See: https://en.wikipedia.org/wiki/List_of_HTTP_status_codes
#    if response.status_code != 200:
#        raise ValueError("Could not retrieve data, code:", response.status_code)

# The service sends JSON data, we parse that into a Python datastructure
    
#stockname = KPN
#currentprice = 11
#high = x
#low = y


