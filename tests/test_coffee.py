import pytest
from customer import Customer
from coffee import Coffee

def test_coffee_name_validation():
    c = Coffee("Mocha")
    assert c.name == "Mocha"

    with pytest.raises(Exception):
        Coffee("ab")  # Name too short

def test_orders_and_customers():
    coffee = Coffee("Espresso")
    c1 = Customer("Alice")
    c2 = Customer("Bob")

    order1 = c1.create_order(coffee, 3.5)
    order2 = c2.create_order(coffee, 4.0)

    assert order1 in coffee.orders()
    assert order2 in coffee.orders()

    customers = coffee.customers()
    assert c1 in customers
    assert c2 in customers

def test_num_orders_and_average_price():
    coffee = Coffee("Cappuccino")
    c1 = Customer("Alice")
    c2 = Customer("Bob")

    c1.create_order(coffee, 4.0)
    c2.create_order(coffee, 6.0)

    assert coffee.num_orders() == 2
    assert coffee.average_price() == 5.0
