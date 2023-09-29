def calculate_money_made(shares, initial_price, final_price):
    """Calculate the money made or lost on a share
       shares int number of shares purchased
       initial_price float price of share when purchased
       final_price float price of share when sold"""
    return shares * (final_price - initial_price)

def main():
    print(calculate_money_made(100, 10, 20),  1000)
    print(calculate_money_made(100, 20, 10), 1000)
    print(calculate_money_made(100, 10, 10), 0)
    print(calculate_money_made(100, 10, 5), -500)


if __name__ == "__main__":
    main()






