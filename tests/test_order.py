import pytest
from customer import Customer
from coffee import Coffee
from order import Order

def test_order_creation_and_price_validation():
    customer = Customer("Alice")
    coffee = Coffee("Americano")

    order = Order(customer, coffee, 3.5)
    assert order.customer == customer
    assert order.coffee == coffee
    assert order.price == 3.5

    with pytest.raises(Exception):
        Order(customer, coffee, 0.5)  # price too low

    with pytest.raises(Exception):
        Order(customer, coffee, 15.0)  # price too high

def test_order_price_immutable():
    order = Order(Customer("Bob"), Coffee("Flat White"), 5.0)
    with pytest.raises(AttributeError):
        order.price = 7.0  # price should be immutable
