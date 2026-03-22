from sqlite3 import Date
from data.Stock import Stock
from data.MounthlyStock import MounthlyStock as MStock
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

if __name__ == "__main__":

    df = pd.read_csv('HistoricalQuotes.csv')
    df[' Close'] = df[' Close'].str.replace('$', '', regex=False).str.replace(',', '', regex=False).astype(float)
    df["Return"] = np.log(df[" Close"] / df[" Close"].shift(1))
    df["mDate"] = pd.to_datetime(df["Date"]).dt.to_period('M')
    ret = df["Return"].groupby(df["mDate"]).sum().reset_index(name="Return")
    ret["signal"] = np.where(ret["Return"] > 0, 1, 0)
    ret["signal"] = ret["signal"].shift(1)
    ret["signal"] = ret["signal"].fillna(0)
    
    ret["signal"] = ret["signal"].astype(int)
    ret["strategy"] = ret["signal"] * ret["Return"]

    res = ret["strategy"].cumsum()
    res2 = ret["Return"].cumsum()
    
    plt.plot(res, label="strategy")
    plt.plot(res2, label="return")
    plt.legend()
    plt.show()