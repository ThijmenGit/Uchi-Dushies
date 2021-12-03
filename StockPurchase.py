import requests

class APIRequest:
    def __init__(self):
        return

    def getstockcode(self):
        query = input("What would you like: ")

        url = (f'https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords={query}&apikey=73R6EIWTFXMUJFO0')
        r = requests.get(url)
        data = r.json()


        for item in range(len(list(data.values())[0])):
            print(list(data.values())[0][item])
            #make data more legible

        stockcode = input("Enter the symbol of the Stock you want to buy: ")
        return stockcode

    def getcurrentvalue(self):
        df = []
        stockname = self.getstockcode()

        response = requests.get(f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={stockname}&outputsize=full&apikey=73R6EIWTFXMUJFO0")
        raw_data = response.json()
        df.append(raw_data['Time Series (Daily)']['2021-12-01'])
        return(df)
        #current date + 5 min series
        #return symbol, name, most recent value

    def getspecificvalue(self, stockdate):
        df = []
        stockname = self.getstockcode()
        response = requests.get(f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={stockname}&outputsize=full&apikey=73R6EIWTFXMUJFO0")
        raw_data = response.json()
        df.append(raw_data['Time Series (Daily)'][str(stockdate)])
        return(df)
        #get date value working



class StockPurchase:
    def __init__(self):
        self.stock_data = {"Apple": 100, "Google": 50}
        self.stock_to_buy = None
        self.stock_price = None


        #Call Stock API
        APIRequest.getcurrentvalue()

        self.stock_to_buy = stock_name
        self.stock_price = self.stock_data[stock_name]
        print(f"The price of {stock_name} is €{self.stock_price}  per stock")
        self.agreed_price()

    def agreed_price(self):
        agreed_price = input(f"Buy the stock at €{self.stock_price} y/n? ")
        if agreed_price.lower() == "n":
            print("Too bad Uchi-Dushi, please insert a different stock name")
            self.stock_name()
        elif agreed_price.lower() != "n" and agreed_price.lower() != "y":
            print("Please insert 'y' or 'n'")
            self.agreed_price()
        self.agreed_amount()
        #feedback to API

    def agreed_amount(self):
        try:
            agreed_amount = int(input(f"How many stocks would you like to buy for €{self.stock_price} per stock? "))
            transaction_price = self.stock_price * agreed_amount
            print(f"Congratulations! You've bought the stock, right on track to become a Sensei!"
                  f"The total amount of this transaction will be €{transaction_price}")
            return
        except ValueError:
            print("This input is not recognized. Please insert a round number")
            self.agreed_amount()


if __name__=="__main__":
    while True:
        stock_purchase = StockPurchase()
        stock_purchase.stock_name()


