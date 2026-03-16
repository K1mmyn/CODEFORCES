class AskNode:
    def __init__(self, ask_price, quantity, id):
        self.ask_price = ask_price
        self.quantity = quantity
        self.userID = id

    def __lt__(self, other):
        if not isinstance(other, AskNode):
            return False

        return self.ask_price < other.ask_price

    def ask_filled(self, quantity):
        self.quantity -= quantity
        return self.quantity

    def get_ask_price(self):
        return self.ask_price

    def get_quantity(self):
        return self.quantity

    def __str__(self):
        return f"Ask Price: {self.ask_price} | Quantity: {self.quantity}"


class AskHeap:
    def __init__(self):
        self.a = []

    """Insert a new element into the Min Heap."""

    def add(self, ask_price, quantity, userID):
        ask = AskNode(ask_price, quantity, userID)
        self.a.append(ask)
        i = len(self.a) - 1
        while (
            i > 0 and self.a[(i - 1) // 2].get_ask_price() > self.a[i].get_ask_price()
        ):
            self.a[i], self.a[(i - 1) // 2] = self.a[(i - 1) // 2], self.a[i]
            i = (i - 1) // 2

    def sale(self, bid_price, quantity):
        lowest_ask_price = self.getMin().get_ask_price()
        if lowest_ask_price <= bid_price:
            if lowest_ask_price - quantity <= 0:
                self.delete(bid_price)
            else:
                self.a[0].ask_filled(quantity)
            return True

        return False

    """Delete a specific element from the Min Heap."""

    def delete(self, bid_price):
        i = -1
        for j in range(len(self.a)):
            if self.a[j].get_ask_price() <= bid_price:
                i = j
                break
        if i == -1:
            return
        self.a[i] = self.a[-1]
        self.a.pop()
        while True:
            left = 2 * i + 1
            right = 2 * i + 2
            smallest = i
            if left < len(self.a) and self.a[left] < self.a[smallest]:
                smallest = left
            if right < len(self.a) and self.a[right] < self.a[smallest]:
                smallest = right
            if smallest != i:
                self.a[i], self.a[smallest] = self.a[smallest], self.a[i]
                i = smallest
            else:
                break

    def getMin(self):
        return self.a[0] if self.a else None

    def __str__(self):
        return "\n".join(str(ask) for ask in self.a)

    def is_empty(self):
        return len(self.a) == 0
