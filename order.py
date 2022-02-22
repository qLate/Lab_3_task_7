

avialable_id = 0


class Order:

    def __init__(self, user_name, location, items, vehicle=None) -> None:
        global avialable_id
        self.orderid = avialable_id
        avialable_id += 1

        self.user_name = user_name
        self.location = location
        self.items = items
        self.vehicle = vehicle

    def __str__(self) -> str:
        return f"order of user {self.user_name} in {self.location.city} with ordered items: \
"+", ".join([item.name for item in self.items])+"."

    def get_price(self):
        return sum([item.price for item in self.items])

    def assign_vehicle(self, vehicle):
        self.vehicle = vehicle
