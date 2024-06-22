
class Coffee:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if isinstance(value, str) and len(value) >= 3:
            self._name = value
        else: 
            raise Exception("name must be a string of at least 3 characters.")
        
    def orders(self):
        return [order for order in Order.all if order.coffee == self and isinstance(order, Order)]
    
    def customers(self):
        coffee_customers = []
        for order in Order.all:
            if order.coffee == self:
                if order.customer not in coffee_customers:
                    if isinstance(order.customer, Customer):
                        coffee_customers.append(order.customer)
        return coffee_customers
    
    def num_orders(self):
        order_total = 0
        for order in Order.all:
            if order.coffee == self:
                order_total += 1
        if order_total == 0:
            return 0
        else:
            return order_total
    
    def average_price(self):
        price_sum = 0
        num_orders = 0
        for order in Order.all:
            if order.coffee == self:
                price_sum += order.price
                num_orders += 1
        if num_orders == 0:
            return 0
        else:
            avg_price = price_sum / num_orders
            return avg_price


class Customer:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if isinstance(value, str) and 1 <= len(value) <= 15:
            self._name = value
        else:
            raise Exception("name must be a string between 1-15 characters.")
        
    def orders(self):
        return [order for order in Order.all if order.customer == self and isinstance(order, Order)]
    
    def coffees(self):
        cust_coffees = []
        for order in Order.all:
            if order.customer == self:
                if order.coffee not in cust_coffees:
                    if isinstance(order.coffee, Coffee):
                        cust_coffees.append(order.coffee)
        return cust_coffees
    
    def create_order(self, coffee, price):
        order = Order(self, coffee, price)
        return order
    
    @classmethod
    def most_aficionado(cls, coffee):
        most_expensive_order = None
        high_price = 0
        for order in cls.orders:
            if order.coffee == coffee:
                if order.price > high_price:
                    high_price = order.price
                    most_expensive_order = order.customer
        if most_expensive_order == None:
            return None
        else:
            return most_expensive_order

    
class Order:

    all = []

    def __init__(self, customer, coffee, price):
        self._customer = customer
        self._coffee = coffee
        self._price = price
        Order.all.append(self)

    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, value):
        if isinstance(value, float) and 1.0 <= value <= 10.0:
            self._price = value
        else:
            raise Exception("price must be a number between 1-10.")
        
    @property 
    def customer(self):
        return self._customer
    
    @customer.setter
    def customer(self, value):
        if isinstance(value, Customer):
            self._customer = value
        else:
            raise Exception("customer must be an instance of Customer.")
        
    @property
    def coffee(self):
        return self._coffee
    
    @coffee.setter
    def coffee(self, value):
        if isinstance(value, Coffee):
            self._coffee = value
        else:
            raise Exception("coffee must be an instance of Coffee.")