import yfinance as yf
from Stock import Stock

if __name__ == "__main__":
    stock = []
    tSymbol = "SIDU"
    ticker = yf.Ticker(tSymbol)
    histData = ticker.history(period="10y")

    for i in range(len(histData)):
        date = histData.index[i].date()

        if i == 0:
            stock.append(Stock(histData["Close"][i], date))
        else:
            stock.append(Stock(histData["Close"][i], date))
            stock[i].set_return_price(stock[i-1].get_price())
    
    for i in range(5):
        print(stock[i].get_date(), stock[i].get_price(), stock[i].get_return_price())
    
    for i in range(len(stock)-5, len(stock)):
        print(stock[i].get_date(), stock[i].get_price(), stock[i].get_return_price())