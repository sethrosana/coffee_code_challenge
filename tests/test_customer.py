import pytest
from customer import Customer
from coffee import Coffee
from order import Order

def test_customer_name_validation():
    c = Customer("Alice")
    assert c.name == "Alice"

    with pytest.raises(Exception):
        c.name = ""

    with pytest.raises(Exception):
        c.name = 100  # Not a string

    c.name = "Bob"
    assert c.name == "Bob"

def test_create_order_and_relationships():
    customer = Customer("Alice")
    coffee = Coffee("Latte")
    order = customer.create_order(coffee, 5.0)

    assert order.customer == customer
    assert order.coffee == coffee
    assert order.price == 5.0

    assert order in customer.orders()
    assert coffee in customer.coffees()

    assert order in coffee.orders()
    assert customer in coffee.customers()
