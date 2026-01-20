import numpy as np
from typing import List
from data.Stock import Stock

class MounthlyStock:
    def __init__(self, price=0.0, date=None, return_price=0.0):
        self.price = price
        self.date = date
        self.return_price = return_price
    
    def get_price(self):
        return self.price

    def get_date(self):
        return self.date

    def set_return_price(self, stocks: List[Stock]):
        self.return_price = np.sum([stock.get_return_price() for stock in stocks])

    def set_return_price(self, return_price):
        self.return_price = return_price

    def get_return_price(self):
        return self.return_price