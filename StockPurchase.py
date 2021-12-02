class StockPurchase:
    def __init__(self):
        self.stock_data = {"Apple": 100, "Google": 50}
        self.stock_to_buy = None
        self.stock_price = None

    def stock_name(self):
        while True:
            stock_name = input("Which stock are you interested in to buy? ")
            if stock_name in self.stock_data:
                break
            else:
                print("This is not an available stock. Please input a valid stock name!")
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

    def agreed_amount(self):
        try:
            agreed_amount = int(input(f"How many stocks would you like to buy for €{self.stock_price} per stock? "))
            transaction_price = self.stock_price * agreed_amount
            print(f"Congratulations! You've bought the stock, right on track to become a Sensei! The total amount of this transaction will be €{transaction_price}")
            return
        except ValueError:
            print("This input is not recognized. Please insert a round number")
            self.agreed_amount()


if __name__=="__main__":
    while True:
        stock_purchase = StockPurchase()
        stock_purchase.stock_name()


