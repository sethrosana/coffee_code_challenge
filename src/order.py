class Order:
    _all = []

    def __init__(self, customer, coffee, price):
        self._validate_price(price)
        self._customer = customer
        self._coffee = coffee
        self._price = price
        Order._all.append(self)

    def _validate_price(self, price):
        if not isinstance(price, float) or not (1.0 <= price <= 10.0):
            raise Exception("Price must be a float between 1.0 and 10.0.")

    @property
    def customer(self):
        return self._customer

    @property
    def coffee(self):
        return self._coffee

    @property
    def price(self):
        return self._price

    @classmethod
    def all(cls):
        return cls._all
