import pandas as pd
from InvestmentGame import APIRequest
import datetime

def agree_price(stock_to_sell):
    agreed_price = ''
    while agreed_price.lower() != "y" and agreed_price.lower() != "n":
        agreed_price = input(f"Do you wish to sell {stock_to_sell['Name']} at {stock_to_sell['Currency']} {stock_to_sell['Price']}? (y/n) ")

    if agreed_price.lower() == 'y':
        return True
    elif agreed_price.lower() == "n":
        return False
    else:
        print("exceptions")

def sell_stock(stock_to_sell):
    try:
        amount = int(input(f"How many stocks would you like to sell? "))
        portfolio = []
        for i in range(amount):
            stock_to_sell["Timestamp"] = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            stock_to_sell["Buy/Sell"] = -1
            portfolio.append(stock_to_sell)
        #print(float(stock_to_sell['Price']))
        #transaction_price = round(float(stock_to_sell['Price']) * amount,3)
        #print(f"The total value of this transaction will be €{transaction_price} ")
        return portfolio
    except ValueError:
            print("This is not a recognized input. Please insert a round number")
            sell_stock(stock_to_sell)

def sell():
    while True:
        portfolio = []
        api = APIRequest()
        stockmetadata = api.getstockmetadata()
        stockprice = APIRequest.getcurrentvalue(stockmetadata)
        stock_info = APIRequest.stockpackage(stockmetadata, stockprice)

        outcome = agree_price(stock_info)
        if outcome == True:
            portfolio = sell_stock(stock_info)
            df = pd.DataFrame(portfolio, columns = ['Tracker', 'Name', 'Region', 'Currency', 'Price', 'Timestamp', 'Buy/Sell'])
            print("Current sell transaction: \n", df, "\n")
            df['Price'] = df['Price'].astype(float)
            portfoliosum = round(df['Price'].sum(),3)
            print(f"The value of this transaction is {stock_info['Currency']} {portfoliosum}")
            return df

        elif outcome == False:
            sell()
        else:
            print("exceptions")


if __name__ == "__main__":
    df = sell()
    print(df)