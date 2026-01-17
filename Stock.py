import numpy as np

class Stock:
    def __init__(self, price=0.0, date=None, return_price=0.0):
        self.price = price
        self.date = date
        self.return_price = return_price

    def get_price(self):
        return self.price   

    def get_date(self):
        return self.date

    def set_return_price(self, prev_price):
        self.return_price = np.log(self.price / prev_price)

    def get_return_price(self):
        return self.return_price