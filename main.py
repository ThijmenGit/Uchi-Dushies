from User import User
import time
from Confirm_price_and_buy1 import purchase
from Confirm_price_and_sell import sell
import pandas as pd

pd.set_option("display.max_rows", None, "display.max_columns", None)
print("Welcome to the investment game Uchi-Dushie! Start playing to become a Sensei Master!")

name = None
while not name:
    name = input("What is your name? ")

print(f"Welkom {name}! Good luke, playing the Investment Game!")
user = User(name)

while True:
    print("------------ MAIN MENU INVESTMENT GAME ------------ ")
    print("[Option 0] Show my balance")
    print("[Option 1] Transfer money to account")
    print("[Option 2] Transfer money from account")
    print("[Option 3] Show my portfolio")
    print("[Option 4] Buy stock")
    print("[Option 5] Sell stock")
    action = input(">>> Enter the number of action you would like to take: ")
    try:
        if int(action) == 0:    # SHOW BALANCE
            print("Your current balance is:")
            print(user.get_balance())
            wait = input("Press enter to continue to the main menu.")
        elif int(action) == 1:  # TRANSFER TO ACCOUNT
            amount = input("How much would you like to transfer to your account? ")
            message = user.transfer_money_to_account(amount)
            print(message)
            wait = input("Press enter to continue to the main menu.")
            time.sleep(2)
        elif int(action) == 2:  # TRANSFER FROM ACCOUNT
            amount = input("How much would you like to transfer from your account? ")
            message = user.transfer_money_from_account(amount)
            print(message)
            wait = input("Press enter to continue to the main menu.")
            time.sleep(2)
        elif int(action) == 3:  # SHOW PORTFOLIO
            print("Your portfolio currently contains the following stocks:")
            print(user.get_portfolio())
            wait = input("Press enter to continue to the main menu.")
        elif int(action) == 4:  # BUY STOCK
            stocks_bought = purchase()
            user.add_stock_to_portfolio(stocks_bought)
            wait = input("Press enter to continue to the main menu.")
        elif int(action) == 5:  # SELL STOCK
            print('hi')
    except ValueError:
        print("!!!!! You didn't enter a menu option number, you can try again in 3 seconds.")
        time.sleep(3)
