import pandas as pd
from InvestmentGame import APIRequest
import datetime



def agree_price(stock_to_buy):
    agreed_price = ''
    while agreed_price.lower() != "y" and agreed_price.lower() != "n":
        print("Please insert 'y' or 'n'")
        agreed_price = input(f"Do you wish to buy {stock_to_buy['Name']} at {stock_to_buy['Currency']} {stock_to_buy['Price']}? (y/n) ")

    if agreed_price.lower() == 'y':
        return True
    elif agreed_price.lower() == "n":
        return False
    else:
        print("exceptions")

def buy_stock(stock_to_buy):
    try:
        amount = int(input(f"How many stocks would you like to buy? "))
        portfolio = []
        for i in range(amount):
            stock_to_buy["Timestamp"] = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            stock_to_buy["Buy/Sell"] = 1
            portfolio.append(stock_to_buy)
        # print(float(stock_to_buy['Price']))
        #transaction_price = round(float(stock_to_buy['Price']) * amount,3)
        #print(f"The total value of this transaction will be €{transaction_price} ")
        return portfolio
    except ValueError:
       print("This is not a recognized input. Please insert a round number")
       buy_stock(stock_to_buy)

#create single function for buying that can be referenced


def purchase():
    while True:
        portfolio = []
        api = APIRequest()
        stockmetadata = api.getstockmetadata()
        stockprice = APIRequest.getcurrentvalue(stockmetadata)
        stock_info = APIRequest.stockpackage(stockmetadata, stockprice)

        outcome = agree_price(stock_info)
        if outcome == True:
            portfolio = buy_stock(stock_info)
            df = pd.DataFrame(portfolio, columns = ['Tracker', 'Name', 'Region', 'Currency', 'Price', 'Timestamp', 'Buy/Sell'])
            df['Price'] = df['Price'].astype(float)
            portfoliosum = round(df['Price'].sum(),3)
            print(f"The value of this transaction is {stock_info['Currency']} {portfoliosum}")
            return df, portfoliosum

        elif outcome == False:
            purchase()
        else:
            print("exceptions")


if __name__ == "__main__":
    df = purchase()
    print(df)