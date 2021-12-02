main
- ask for name. Create user if user does not exist or load user data.
- ask what user wants to do: buy / sell / show portfolio

User
- setName
- getName
- getPortfolio
- addStockToPortfolio
- removeStockFromPortfolio

AlphaAdvantageAPI
- searchForStocks
- getCurrentPriceForStock
- getPriceOnDateForStock(stock_name, date)

Stock (alleen nodig als we complexe dingen gaan doen met de data die uit de API komt)
- setName
- getCurrentPrice
- getPriceOnDate

StockPurchase
- buyStock
- _enterAmount