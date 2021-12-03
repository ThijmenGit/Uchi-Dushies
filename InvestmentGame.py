import requests



class APIRequest:
    def __init__(self):
        return

    def getstockcode(self):
        query = input("What would you like: ")

        url = (f'https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords={query}&apikey=73R6EIWTFXMUJFO0')
        r = requests.get(url)
        data = r.json()

        #first_key = list(colors)[0]
        #first_val = list(colors.values())[0]

        for item in range(len(list(data.values())[0])):
            print(list(data.values())[0][item])

        stockcode = input("Enter the symbol of the Stock you want to buy: ")
        return stockcode

    def getcurrentvalue(self):
        df = []
        stockname = self.getstockcode()

        response = requests.get(f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={stockname}&outputsize=full&apikey=73R6EIWTFXMUJFO0")
        raw_data = response.json()
        df.append(raw_data['Time Series (Daily)']['2021-12-01'])
        return(df)

    def getspecificvalue(self, stockdate):
        df = []
        stockname = self.getstockcode()
        response = requests.get(f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={stockname}&outputsize=full&apikey=73R6EIWTFXMUJFO0")
        raw_data = response.json()
        df.append(raw_data['Time Series (Daily)'][str(stockdate)])
        return(df)


if __name__=="__main__":
    API = APIRequest()
    df = API.getspecificvalue('2020-01-01')
    print(df)
    #date





#    car = Car()
#    car.drive(10)
#    car.drive(350)
#    print(car)

# Since we are retrieving stuff from a web service, it's a good idea to check for the return status code
# See: https://en.wikipedia.org/wiki/List_of_HTTP_status_codes
#    if response.status_code != 200:
#        raise ValueError("Could not retrieve data, code:", response.status_code)

# The service sends JSON data, we parse that into a Python datastructure
    
#stockname = KPN
#currentprice = 11
#high = x
#low = y


