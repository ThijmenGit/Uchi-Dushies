import pandas as pd

portfolio = []
df = pd.DataFrame(portfolio, columns = ['Tracker', 'Name', 'Region', 'Currency', 'Buyingprice'])

def agree_price():
    agreed_price = ''
    while agreed_price.lower() != "y" and agreed_price.lower() != "n":
        print("Please insert 'y' or 'n'")
        agreed_price = input("Do you wish to buy y/n? ")

    if agreed_price.lower() == 'y':
        return True
    elif agreed_price.lower() == "n":
        print("Too bad Uchi-Dushi")
        return False
    else:
        print("exceptions")

def buy_stock():
    try:
        amount = int(input(f"How many stocks would you like to buy? "))
        stock_to_buy = {"Name": "Apple", "Region": "Amsterdam", "Currency": "euros","Buyingprice": 350}  ## getstockprice()
        for i in range(amount):
            portfolio.append(f"{stock_to_buy}")
        transaction_price = stock_to_buy["Buyingprice"] * amount
        print(f"The total costs of this transaction will be €{transaction_price} ")
        return transaction_price
    except ValueError:
        print("This is not a recognized input. Please insert a round number")
        buy_stock()


outcome = agree_price()
if outcome == True:
    print("Got it")
    buy_stock()
    print("Current portfolio holds", df)
elif outcome == False:
    print("Moving back up")
    ## Refer back to code Thijmen to check different stockname + price
else:
    print("exceptions")