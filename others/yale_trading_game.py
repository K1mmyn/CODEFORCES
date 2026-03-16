import random

suits = ["H", "D", "C", "S"]
deck = {
    "H": [
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "10",
        "J",
        "Q",
        "K",
        "A",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "10",
        "J",
        "Q",
        "K",
        "A",
    ],
    "D": [
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "10",
        "J",
        "Q",
        "K",
        "A",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "10",
        "J",
        "Q",
        "K",
        "A",
    ],
    "C": [
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "10",
        "J",
        "Q",
        "K",
        "A",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "10",
        "J",
        "Q",
        "K",
        "A",
    ],
    "S": [
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "10",
        "J",
        "Q",
        "K",
        "A",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "10",
        "J",
        "Q",
        "K",
        "A",
    ],
}

stocks = {}

# ! EDGE PCIKING A SUIT WITH NO CARDS LEFT


def calculate_total_value(cards):
    total_value = 0
    for i in range(len(cards)):
        suit, face_value = cards[i][0], cards[i][1:]
        value = 0
        if face_value == "A":
            value = 20
        elif face_value in "KJQ":
            value = 10
        else:
            value = int(face_value)

        if suit in "CS":
            value *= 2
        elif suit in "HD":
            value *= -1

        total_value += value

    return total_value


def get_random_card():
    suit_index = random.randint(0, len(suits) - 1)
    suit = suits[suit_index]

    while len(deck[suit]) == 0:
        deck.pop(suit)
        suits.pop(suit_index)
        suit = suits[random.randint(0, len(deck) - 1)]

    card_index = random.randint(0, len(deck[suit]) - 1)
    face_value = deck[suit][card_index]
    deck[suit].pop(card_index)

    return suit, face_value


for i in range(4):
    stocks[i] = {"cards": [], "total": 0, "SAR": 20, "EPS": 0}
    for _ in range(10):
        suit, face_value = get_random_card()
        stocks[i]["cards"].append(f"{suit}{face_value}")

    stocks[i]["total"] = calculate_total_value(stocks[i]["cards"])

    already_picked = []

    # SAR

    for j in range(5):
        ran_card_index = random.randint(0, 9)
        while ran_card_index in already_picked:
            ran_card_index = random.randint(0, 9)

        already_picked.append(ran_card_index)

    for j in range(5):
        already_picked[j] = stocks[i]["cards"][already_picked[j]]

    stocks[i]["SAR"] += calculate_total_value(already_picked)

    # EPS

    for j in range(1):
        total = stocks[i]["total"]
        eps_value = total

        ran_card = random.randint(0, len(stocks[i]["cards"]) - 1)
        removed_card = stocks[i]["cards"].pop(ran_card)
        eps_value -= calculate_total_value([removed_card])

        #! ADD CARD BACK INTO DECK

        suit, face_value = get_random_card()
        new_card = f"{suit}{face_value}"
        stocks[i]["cards"].append(new_card)
        eps_value += calculate_total_value([new_card])

        eps_value -= total
        stocks[i]["EPS"] = eps_value

print(stocks)


def peek(stock):
    already_picked = []

    for j in range(3):
        ran_card_index = random.randint(0, 9)
        while ran_card_index in already_picked:
            ran_card_index = random.randint(0, 9)

        already_picked.append(stocks[stock]["cards"][ran_card_index])

    print(already_picked)
