import pandas as pd
from datetime import datetime
import os


pd.set_option("display.max_rows", None, "display.max_columns", None)

class User:
    def __init__(self, name):
        self.name = name
        self.balance = 0
        self.csv_file_path = f'./portfolio_data/{name}'
        if os.path.isfile(self.csv_file_path):
            # existing user, load portfolio
            self.portfolio = pd.read_csv(self.csv_file_path)
        else:
            # new user, start with empty portfolio
            self.portfolio = pd.DataFrame(None, columns=['Tracker', 'Name', 'Region', 'Currency', 'Price', 'Timestamp', 'Buy/Sell'])

    def _write_portfolio_to_file(self):
        df_csv = self.portfolio.to_csv(index=False)
        f = open(self.csv_file_path, "w")
        f.write(df_csv)
        f.close()
        return True

    def get_balance(self):
        return self.balance

    def get_portfolio(self):
        grouped_by_stock = self.portfolio.groupby(
            ['Name'])['Buy/Sell'].agg('sum')
        return grouped_by_stock.to_string()

    def add_stock_to_portfolio(self, stock_df):
        # print("DF PORTFOLIO -------------------------")
        # print(self.portfolio)
        # print("STOCKS BOUGHT PORTFOLIO -------------------------")
        # print(stock_df)
        # print("MERGED PORTFOLIO -------------------------")
        self.portfolio = self.portfolio.append(stock_df)
        # print(self.portfolio)
        self._write_portfolio_to_file()
        return True

    def remove_stock_from_portfolio(self, stock_df):
        # todo check if stocks can be sold before appending to prevent < 0
        self.portfolio = self.portfolio.append(stock_df)
        self._write_portfolio_to_file()
        return True

    def transfer_money_to_account(self, amount):
        if not amount.isnumeric():
            return "You didn't enter a numeric value, please try again."
        self.balance = self.balance + int(amount)
        return f"Transaction succeeded, your new balance is {self.balance}"

    def transfer_money_from_account(self, amount):
        if not amount.isnumeric():
            return "You didn't enter a numeric value, please try again."
        if self.balance < int(amount):
            return "Your balance is not sufficient to withdraw this amount of money. Try again."
        self.balance = self.balance - int(amount)
        return f"Transaction succeeded, your new balance is {self.balance}"


if __name__ == "__main__":
    luke = User('Luke')
    luke.add_stock_to_portfolio({'Tracker': 'KPN.AMS', 'Name': 'Koninklijke KPN N.V.', 'Region': 'Amsterdam', 'Currency': 'Eur', 'TransactionPrice': '2.78'})
    luke.add_stock_to_portfolio({'Tracker': 'KPN.AMS', 'Name': 'Koninklijke KPN N.V.', 'Region': 'Amsterdam', 'Currency': 'Eur', 'TransactionPrice': '2.78'})
    luke.remove_stock_from_portfolio({'Tracker': 'KPN.AMS', 'Name': 'Koninklijke KPN N.V.', 'Region': 'Amsterdam', 'Currency': 'Eur', 'TransactionPrice': '2.78'})
    luke.add_stock_to_portfolio({'Tracker': 'KPN.AMS', 'Name': 'Koninklijke KPN N.V.', 'Region': 'Amsterdam', 'Currency': 'Eur', 'TransactionPrice': '2.78'})
    print(luke.get_portfolio())
