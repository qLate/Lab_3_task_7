class Item:

    def __init__(self, name, price) -> None:
        self.name = name
        self.price = price

    def __str__(self) -> str:
        return f"Item name is {self.name} and it costs {self.price} UAN"
