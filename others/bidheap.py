class BidNode:
    def __init__(self, bid_price, userID, quantity):
        self.bid_price = bid_price
        self.userID = userID
        self.quantity = quantity

    def __gt__(self, other):
        if not isinstance(other, BidNode):
            return False

        return self.bid_price > other.bid_price

    def get_bid_price(self):
        return self.bid_price

    def get_quantity(self):
        return self.quantity

    def __str__(self):
        return f"Bid Price: {self.bid_price}"


class BidHeap:
    def __init__(self):
        self.a = []

    """Insert a new element into the Max Heap."""

    def add(self, bid_price, userID, quantity):
        bid = BidNode(bid_price, userID, quantity)
        self.a.append(bid)
        i = len(self.a) - 1
        while (
            i > 0 and self.a[(i - 1) // 2].get_bid_price() < self.a[i].get_bid_price()
        ):
            self.a[i], self.a[(i - 1) // 2] = self.a[(i - 1) // 2], self.a[i]
            i = (i - 1) // 2

    """Delete a specific element from the Max Heap."""

    def delete(self, bid_price):
        i = -1
        for j in range(len(self.a)):
            if self.a[j].get_bid_price() == bid_price:
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

    def getMax(self):
        return self.a[0] if self.a else None

    def __str__(self):
        return "\n".join(str(bid) for bid in self.a)

    def is_empty(self):
        return len(self.a) == 0
