import yfinance as yf

if __name__ == "__main__":
    stock = []
    tSymbol = "SIDU"
    ticker = yf.Ticker(tSymbol)
    histData = ticker.history(period="10y")

    for date, price in histData.iterrows():
        stock.append(Stock(price, date))

    print(stock)