import pandas as pd
from InvestmentGame import APIRequest

portfolio = []

stockmetadata = APIRequest.getstockmetadata()
stockprice = APIRequest.getcurrentvalue(stockmetadata)
stock_to_buy = APIRequest.stockpackage(stockmetadata, stockprice)

def agree_price():
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

def buy_stock():
    try:
        amount = int(input(f"How many stocks would you like to buy? "))
        for i in range(amount):
            portfolio.append(stock_to_buy)
        print(float(stock_to_buy['Buyingprice']))
        transaction_price = round(float(stock_to_buy['Buyingprice']) * amount,3)
        print(f"The total value of this transaction will be €{transaction_price} ")
        return transaction_price
    except ValueError:
       print("This is not a recognized input. Please insert a round number")
       buy_stock()

while True:
    outcome = agree_price()
    if outcome == True:
        buy_stock()
        df = pd.DataFrame(portfolio, columns = ['Tracker', 'Name', 'Region', 'Currency', 'Buyingprice'])
        print("Current portfolio holds: \n", df, "\n") ## Insert dataframe here?
        df['Buyingprice'] = df['Buyingprice'].astype(float)
        portfoliosum = round(df['Buyingprice'].sum(),3)
        print(f"The value of this transaction is {stock_to_buy['Currency']} {portfoliosum}")
        break

    elif outcome == False:
        stockmetadata = APIRequest.getstockmetadata()
        stockprice = APIRequest.getcurrentvalue(stockmetadata)
        stock_to_buy = APIRequest.stockpackage(stockmetadata, stockprice)
        ## Refer back to code Thijmen to check different stockname + price
    else:
        print("exceptions")