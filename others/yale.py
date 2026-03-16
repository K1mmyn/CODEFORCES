import random
from bidheap import BidHeap
from askheap import AskHeap


class Player:
    def __init__(self, id: int):
        self.id = id
        self.cash = 500
        self.portfolio = {i: 5 for i in range(4)}

    def get_cash_balance(self):
        return self.cash

    def get_portfolio(self):
        return self.portfolio

    def get_shares_in_stock(self, stock):
        return self.portfolio[stock]

    def sell_shares(self, stock, quantity):
        self.portfolio[stock] -= quantity
        return

    def buy_shares(self, bid_price, quantity):
        self.cash -= quantity * bid_price
        return


class Yale_Trading_Game:

    def __init__(self, amount_of_players: int):
        self.deck = {
            "H": {
                "2": {"quantity": 2, "value": 2},
                "3": {"quantity": 2, "value": 3},
                "4": {"quantity": 2, "value": 4},
                "5": {"quantity": 2, "value": 5},
                "6": {"quantity": 2, "value": 6},
                "7": {"quantity": 2, "value": 7},
                "8": {"quantity": 2, "value": 8},
                "9": {"quantity": 2, "value": 9},
                "10": {"quantity": 2, "value": 10},
                "J": {"quantity": 2, "value": 10},
                "Q": {"quantity": 2, "value": 10},
                "K": {"quantity": 2, "value": 10},
                "A": {"quantity": 2, "value": 20},
            },
            "D": {
                "2": {"quantity": 2, "value": 2},
                "3": {"quantity": 2, "value": 3},
                "4": {"quantity": 2, "value": 4},
                "5": {"quantity": 2, "value": 5},
                "6": {"quantity": 2, "value": 6},
                "7": {"quantity": 2, "value": 7},
                "8": {"quantity": 2, "value": 8},
                "9": {"quantity": 2, "value": 9},
                "10": {"quantity": 2, "value": 10},
                "J": {"quantity": 2, "value": 10},
                "Q": {"quantity": 2, "value": 10},
                "K": {"quantity": 2, "value": 10},
                "A": {"quantity": 2, "value": 20},
            },
            "C": {
                "2": {"quantity": 2, "value": 2},
                "3": {"quantity": 2, "value": 3},
                "4": {"quantity": 2, "value": 4},
                "5": {"quantity": 2, "value": 5},
                "6": {"quantity": 2, "value": 6},
                "7": {"quantity": 2, "value": 7},
                "8": {"quantity": 2, "value": 8},
                "9": {"quantity": 2, "value": 9},
                "10": {"quantity": 2, "value": 10},
                "J": {"quantity": 2, "value": 10},
                "Q": {"quantity": 2, "value": 10},
                "K": {"quantity": 2, "value": 10},
                "A": {"quantity": 2, "value": 20},
            },
            "S": {
                "2": {"quantity": 2, "value": 2},
                "3": {"quantity": 2, "value": 3},
                "4": {"quantity": 2, "value": 4},
                "5": {"quantity": 2, "value": 5},
                "6": {"quantity": 2, "value": 6},
                "7": {"quantity": 2, "value": 7},
                "8": {"quantity": 2, "value": 8},
                "9": {"quantity": 2, "value": 9},
                "10": {"quantity": 2, "value": 10},
                "J": {"quantity": 2, "value": 10},
                "Q": {"quantity": 2, "value": 10},
                "K": {"quantity": 2, "value": 10},
                "A": {"quantity": 2, "value": 20},
            },
        }
        self.suits = ["H", "D", "C", "S"]
        self.stocks = {}
        self.asks = {}
        self.bids = {}

        for i in range(4):
            self.stocks[i] = {"cards": [], "SAR": 0, "EPS": 0}
            self.bids[i] = BidHeap()
            self.asks[i] = AskHeap()
            for j in range(10):
                random_card = self.get_random_card_from_deck()
                self.stocks[i]["cards"].append(random_card)

            self.stocks[i]["SAR"] = self.calculate_SAR(i)

        self.amount_of_players = amount_of_players
        self.players = {i: Player(i) for i in range(amount_of_players)}

    def get_amount_of_players(self) -> int:
        return self.amount_of_players

    def get_user_shares(self, id, stock):
        return self.players[id].get_shares_in_stock(stock)

    def get_user_cash(self, id):
        return self.players[id].get_cash_balance()

    def add_ask_order(self, ask_price, quantity, userID, stock):
        self.players[userID].sell_shares(stock, quantity)
        return self.asks[stock].add(ask_price, quantity, userID)

    def add_bid_order(self, bid_price, quantity, userID, stock):
        self.players[userID].buy_shares(bid_price, quantity)
        return self.bids[stock].add(bid_price, userID, quantity)

    def get_user_input(
        self,
        min_input: int,
        max_input: int,
        prompt: str = "",
    ):
        while True:
            try:
                user_input = int(input(prompt))
                if user_input < min_input or user_input > max_input:
                    raise ValueError()
                else:
                    return user_input

            except ValueError:
                print(f"Please enter an number between {min_input}-{max_input}")

    def print_asks(self):
        print("Current Asks on Market")
        for stock in self.asks.keys():
            print(f"Company {stock}", str(self.asks[stock]))

    def print_bids(self):
        print("Current Bids on Market")
        for stock in self.bids.keys():
            print(f"Company {stock}", str(self.bids[stock]))

    def begin(self, amount_of_turns: int):
        print(
            "Welcome to the AQS Yale Trading Game\nCommands:\n(0) Peek at 3 hidden cards of a stock\n(1) Place a Ask Order\n(2) Place a Bid Order"
        )
        for i in range(amount_of_turns):
            self.print_asks()
            self.print_bids()

            current_player = i % self.get_amount_of_players()
            command = self.get_user_input(0, 2, f"\nUser {current_player} Turn: ")
            stock = self.get_user_input(0, 3, "Select a stock 0-3\n")

            match command:
                # Peek at a stock
                case 0:
                    print(f"\nRandom cards from stock {stock} {self.peek(stock)} \n")
                    continue
                case 1:
                    user_shares = self.get_user_shares(current_player, stock)
                    quantity = self.get_user_input(
                        1,
                        user_shares,
                        f"You currently have {user_shares} amount of shares in company {stock}, How many shares would you like to sell?\n",
                    )
                    price = self.get_user_input(
                        0,
                        float("inf"),
                        f"What price would you like to sell at?\n",
                    )
                    self.add_ask_order(quantity, price, current_player, stock)
                    continue
                case 2:
                    user_cash = self.get_user_cash(current_player)
                    quantity = self.get_user_input(
                        1,
                        float("inf"),
                        f"How many shares would you like to buy? You currently have ${user_cash}\n",
                    )
                    price = self.get_user_input(
                        0,
                        float("inf"),
                        f"What price would you like to buy at?\n",
                    )

                    self.add_bid_order(price, quantity, current_player, stock)
                    # while self.asks[stock].is_empty():
                    #     print("There are no active ask orders for this stock. Please select a different stock to buy")
                    #     stock = self.get_user_input(0, 3, "Select a stock 0-3\n")

                    # user_cash = self.get_user_cash()
                    # shares_for_sale = self.asks[stock].getMin().get_quanity()
                    # price = self.asks[stock].getMin().get_ask_price()
                    # quantity = self.get_user_input(
                    #     1,
                    #     shares_for_sale,
                    #     f"You currently have ${user_cash}, The current lowest ask for company {stock} is {shares_for_sale} shares at ${price}\n",
                    # )

                    continue

        return

    def get_random_card_from_deck(self):
        suit = random.choice(self.suits)

        cards_availble = [
            face_value
            for face_value in self.deck[suit].keys()
            if self.deck[suit][face_value]["quantity"] > 0
        ]

        while len(cards_availble) == 0:
            suit = random.choice(self.suits)
            cards_availble = [
                card
                for card in self.stocks[suit].keys()
                if self.stocks[suit]["quantity"] > 0
            ]

        random_card = random.choice(cards_availble)
        self.deck[suit][random_card]["quantity"] -= 1
        return f"{suit}{random_card}"

    def get_total_value(self, stock):
        total = sum(
            self.calculate_card_value(card) for card in self.stocks[stock]["cards"]
        )
        return total

    def calculate_card_value(self, card):
        suit, face_value = card[0], card[1:]
        value = self.deck[suit][face_value]["value"]

        if suit in "CS":
            value *= 2
        elif suit in "HD":
            value *= -1

        return value

    def calculate_SAR(self, stock):
        SAR = sum(
            self.calculate_card_value(self.stocks[stock]["cards"][index])
            for index in random.sample(range(1, 10), 5)
        )

        return SAR

    def calculate_EPS(self, stock):
        total = self.get_total_value(stock)
        eps_value = total

        random_card = self.stocks[stock]["cards"].pop(random.randint(0, 9))
        eps_value -= self.calculate_card_value(random_card)

        suit, face_value = random_card[0], random_card[1:]
        self.deck[suit][face_value]["quantity"] += 1

        new_card = self.get_random_card_from_deck()
        self.stocks[stock]["cards"].append(new_card)
        eps_value += self.calculate_card_value(new_card)

        eps_value -= total
        return eps_value

    def peek(self, stock):
        return " ".join(
            self.stocks[stock]["cards"][index]
            for index in random.sample(range(1, 10), 3)
        )

    def get_stocks(self):
        return self.stocks

    def get_deck(self):
        return self.deck


obj = Yale_Trading_Game(2)
obj.begin(10)
