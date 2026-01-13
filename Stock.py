class Stock:
    def __init__(self, price=0.0, date=None):
        self.price = price
        self.date = date

    def get_price(self):
        return self.price

    def get_date(self):
        return self.date
