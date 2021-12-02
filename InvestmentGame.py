import requests

def Getstockcode():

query = input("What would you like: ")

url = (f'https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords={query}&apikey=73R6EIWTFXMUJFO0')
r = requests.get(url)
data = r.json()

#first_key = list(colors)[0]
#first_val = list(colors.values())[0]

for item in range(len(list(data.values())[0])):
    print(list(data.values())[0][item])

stockname = input("Enter the symbol of the Stock you want to buy")

df=[]

response = requests.get(f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={stockname}&outputsize=full&apikey=73R6EIWTFXMUJFO0")
raw_data = response.json()
df.append(raw_data['Time Series (Daily)']['2021-12-01']
print(df)


# Since we are retrieving stuff from a web service, it's a good idea to check for the return status code
# See: https://en.wikipedia.org/wiki/List_of_HTTP_status_codes
#    if response.status_code != 200:
#        raise ValueError("Could not retrieve data, code:", response.status_code)

# The service sends JSON data, we parse that into a Python datastructure
    
#stockname = KPN
#currentprice = 11
#high = x
#low = y


