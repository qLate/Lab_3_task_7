from typing import List
from item import Item
from order import Order
from vehicle import Vehicle
from location import Location


class LogisticSystem:

    def __init__(self, vehicles, orders: List[Order] = []) -> None:
        self.orders = orders
        self.vehicles = vehicles

    def placeOrder(self, order):
        vehicle = self.get_free_vehicle()
        if vehicle:
            order.assign_vehicle(vehicle)
            vehicle.avialable = False
            self.orders.append(order)
        else:
            print("No vehicle avialable at the moment.")

    def trackOrder(self, orderid):
        order = self.find_order(orderid)
        if order:
            print(f"Your order #{orderid} is sent to {order.location.city}. \
Total price: {order.get_price()} UAH.")

    def find_order(self, orderid):
        for order in self.orders:
            if order.orderid == orderid:
                return order
        print("No such order.")

    def get_free_vehicle(self):
        for vehicle in self.vehicles:
            if vehicle.avialable:
                return vehicle


vehicles = [Vehicle(1), Vehicle(2)]

logSystem = LogisticSystem(vehicles)
my_items = [Item('book', 110), Item('chupachups', 44)]
my_order = Order('Oleg', Location('Lviv', 53), my_items)

logSystem.placeOrder(my_order)
logSystem.trackOrder(0)

my_items2 = [Item('flowers', 11), Item('shoes', 153), Item('helicopter', 0.33)]

my_order2 = Order('Andrii', Location('Odessa', 3), my_items2)

logSystem.placeOrder(my_order2)
logSystem.trackOrder(1)


my_items3 = [Item('coat', 61.8), Item('shower', 5070), Item('rollers', 700)]

my_order3 = Order("Olesya", Location('Kharkiv', 17), my_items3)

logSystem.placeOrder(my_order3)

logSystem.trackOrder(2)

print(my_order)
