class Stock:
    __slots__ = ("name", "_shares", "_price")

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if not isinstance(value, float):
            raise TypeError("Expected float")

        self._price = value

    @property
    def shares(self):
        return self._shares

    @shares.setter
    def shares(self, value):
        if not isinstance(value, int):
            raise TypeError("Expected int")

        self._shares = value

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, shares):
        if shares > self.shares:
            raise RuntimeError("no enough stocks")
        self.shares -= shares

    def __repr__(self) -> str:
        return f"Stock({self.name}, {self.shares}, {self.price})"


class MyStock(Stock):
    def __init__(self, name, shares, price, factor):
        super().__init__(name, shares, price)
        self.factor = factor

    def panic(self):
        self.sell(self.shares)

    @property
    def cost(self):
        return self.factor * super().cost
