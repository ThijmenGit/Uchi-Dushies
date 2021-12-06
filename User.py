import pandas as pd
from datetime import datetime


class User:
    def __init__(self, name):
        self.name = name
        self.portfolio = pd.DataFrame(None, columns=['Tracker', 'Name', 'Region', 'Currency', 'TransactionPrice',
                                                     'TransactionDate', 'BuyOrSell'])
        # todo if data file exists, load portfolio

    def get_portfolio(self):
        grouped_by_stock = self.portfolio.groupby(['Tracker'])['BuyOrSell'].agg('sum')
        return grouped_by_stock

    def add_stock_to_portfolio(self, stock):
        try:
            self.portfolio = self.portfolio.append({
                'Tracker': stock['Tracker'],
                'Name': stock['Name'],
                'Region': stock['Region'],
                'Currency': stock['Currency'],
                'TransactionPrice': stock['TransactionPrice'],
                'TransactionDate': datetime.today(),
                'BuyOrSell': 1
            }, ignore_index=True)
            return True
        except KeyError:
            print("Stock not removed from portfolio, one of the input fields was not provided")
            return False

    def remove_stock_from_portfolio(self, stock):
        try:
            self.portfolio = self.portfolio.append({
                'Tracker': stock['Tracker'],
                'Name': stock['Name'],
                'Region': stock['Region'],
                'Currency': stock['Currency'],
                'TransactionPrice': stock['TransactionPrice'],
                'TransactionDate': datetime.today(),
                'BuyOrSell': -1
            }, ignore_index=True)
            return True
        except KeyError:
            print("Stock not removed from portfolio, one of the input fields was not provided")
            return False


if __name__ == "__main__":
    luke = User('Luke')
    luke.add_stock_to_portfolio({'Tracker': 'KPN.AMS', 'Name': 'Koninklijke KPN N.V.', 'Region': 'Amsterdam', 'Currency': 'Eur', 'TransactionPrice': '2.78'})
    luke.add_stock_to_portfolio({'Tracker': 'KPN.AMS', 'Name': 'Koninklijke KPN N.V.', 'Region': 'Amsterdam', 'Currency': 'Eur', 'TransactionPrice': '2.78'})
    luke.remove_stock_from_portfolio({'Tracker': 'KPN.AMS', 'Name': 'Koninklijke KPN N.V.', 'Region': 'Amsterdam', 'Currency': 'Eur', 'TransactionPrice': '2.78'})
    print(luke.get_portfolio())
