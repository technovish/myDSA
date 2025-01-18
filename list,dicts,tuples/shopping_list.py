shopping_list = {"banana":5, "orange":4, "apple":3}
stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}

prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

def compute_bill(food):
    total = 0
    for number in food:
        print(food[number])
        if (food[number] <= stock[number]):
            total += prices[number] * food[number]
            stock[number] -= food[number]
        else:
            total += prices[number] * stock[number]
            stock[number] -= food[number]
    print(total)
    print(stock)

compute_bill(shopping_list)
