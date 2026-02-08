import yfinance as yf
from data.Stock import Stock
from data.MounthlyStock import MounthlyStock as MStock
import pandas as pd

if __name__ == "__main__":
    stock = []
    mounthly_stock = []
    tSymbol = "AAPL"
    ticker = yf.Ticker(tSymbol)
    histData = ticker.history(period="1y")

    for i in range(len(histData)):
        date = histData.index[i]

        if i == 0:
            stock.append(Stock(histData["Close"][i], date))
            histData.at[date, "return_price"] = 0.0
        else:
            stock.append(Stock(histData["Close"][i], date))
            stock[i].set_return_price(stock[i-1].get_price())
            histData.at[date, "return_price"] = stock[i].get_return_price()

    # Due to issues with efinance library I have to change the data source for my project