import yfinance as yf
from data.Stock import Stock
from data.MounthlyStock import MounthlyStock as MStock
import pandas as pd

if __name__ == "__main__":
    stock = []
    mounthly_stock = []
    tSymbol = "SIDU"
    ticker = yf.Ticker(tSymbol)
    histData = ticker.history(period="10y")

    for i in range(len(histData)):
        date = histData.index[i]

        if i == 0:
            stock.append(Stock(histData["Close"][i], date))
            histData.at[date, "return_price"] = 0.0
        else:
            stock.append(Stock(histData["Close"][i], date))
            stock[i].set_return_price(stock[i-1].get_price())
            histData.at[date, "return_price"] = stock[i].get_return_price()

    # monthly_data = pd.DataFrame()
    # monthly_data["date"] = histData.resample("ME").first().index.date
    # monthly_data["price"] = histData["Close"].resample("ME").mean()
    # monthly_data["return"] = histData["return_price"].resample("ME").sum()

    monthly_date = histData.resample("ME").first().index.date
    monthly_data = histData["Close"].resample("ME").mean()
    monthly_return = histData["return_price"].resample("ME").sum()

    for i in range(len(monthly_data)):
        mounthly_stock.append(MStock(monthly_data[i], monthly_date[i], monthly_return[i]))
        print(monthly_data[i], monthly_date[i], monthly_return[i])