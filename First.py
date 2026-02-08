from sqlite3 import Date
from data.Stock import Stock
from data.MounthlyStock import MounthlyStock as MStock
import pandas as pd
import numpy as np

if __name__ == "__main__":

    df = pd.read_csv('HistoricalQuotes.csv')
    df[' Close'] = df[' Close'].str.replace('$', '', regex=False).str.replace(',', '', regex=False).astype(float)
    df["Return"] = np.log(df[" Close"] / df[" Close"].shift(1))
    
    print(df["Date"])