import pandas as pd
from InvestmentGame import APIRequest
import datetime



def agree_price(stock_to_buy):
    agreed_price = ''
    while agreed_price.lower() != "y" and agreed_price.lower() != "n":
        print("Please insert 'y' or 'n'")
        agreed_price = input(f"Do you wish to buy {stock_to_buy['Name']} at {stock_to_buy['Currency']} {stock_to_buy['Buyingprice']}? (y/n) ")

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
        print(float(stock_to_buy['Buyingprice']))
        transaction_price = round(float(stock_to_buy['Buyingprice']) * amount,3)
        print(f"The total value of this transaction will be €{transaction_price} ")
        return portfolio
    except ValueError:
       print("This is not a recognized input. Please insert a round number")
       buy_stock(stock_to_buy)

#create single function for buying that can be referenced


def purchase():
    while True:
        portfolio = []
        stockmetadata = APIRequest.getstockmetadata()
        stockprice = APIRequest.getcurrentvalue(stockmetadata)
        stock_to_buy = APIRequest.stockpackage(stockmetadata, stockprice)

        outcome = agree_price(stock_to_buy)
        if outcome == True:
            portfolio = buy_stock(stock_to_buy)
            df = pd.DataFrame(portfolio, columns = ['Tracker', 'Name', 'Region', 'Currency', 'Buyingprice', 'Timestamp', 'Buy/Sell'])
            print("Current portfolio holds: \n", df, "\n") ## Insert dataframe here?
            df['Buyingprice'] = df['Buyingprice'].astype(float)
            portfoliosum = round(df['Buyingprice'].sum(),3)
            print(f"The value of this transaction is {stock_to_buy['Currency']} {portfoliosum}")
            return df

        elif outcome == False:
            purchase()
        else:
            print("exceptions")

df = purchase()
print(df)