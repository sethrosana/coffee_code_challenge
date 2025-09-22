from order import Order

class Coffee:
    _all = []

    def __init__(self, name):
        self._validate_name(name)
        self._name = name
        Coffee._all.append(self)

    @property
    def name(self):
        return self._name

    def _validate_name(self, name):
        if not isinstance(name, str) or len(name) < 3:
            raise Exception("Coffee name must be a string with at least 3 characters.")

    def orders(self):
        return [order for order in Order.all() if order.coffee == self]

    def customers(self):
        return list({order.customer for order in self.orders()})

    def num_orders(self):
        return len(self.orders())

    def average_price(self):
        orders = self.orders()
        if not orders:
            return 0
        return sum(order.price for order in orders) / len(orders)

    @classmethod
    def all(cls):
        return cls._all

    @classmethod
    def most_aficionado(cls, coffee):
        customer_totals = {}
        for order in coffee.orders():
            customer = order.customer
            customer_totals[customer] = customer_totals.get(customer, 0) + order.price

        if not customer_totals:
            return None
        return max(customer_totals, key=customer_totals.get)
