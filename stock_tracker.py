def display_available_stocks(stock_prices):

    print("Available Stocks:")

    for stock, price in stock_prices.items():
        print(f"{stock} : ${price}")


def get_valid_stock(stock_prices):

    stock = input("Enter stock name: ").upper()

    while stock not in stock_prices: 
        print("Invalid stock! Please choose from the available stocks.")
        stock = input("Enter the stock name: ").upper()
    return stock 
    

def calculate_portfolio(stock, stock_prices, total):
    quantity = int(input("Enter quantity: "))

    investment = stock_prices[stock] * quantity

    total += investment
    print(f"\nInvestment value: ${investment}")
    
    return total


def save_portfolio(total):
    with open("portfolio.txt","w") as file:
        file.write("========== Portfolio Summary ==========\n")
        file.write(f"Total Invested Value: ${total}\n")
        file.write("=======================================\n")
        

def print_summary(total):

    print("\n========== Portfolio Summary ==========")
    print(f"Total Invested Value: ${total}")
    print("=======================================")

def main():
    
    stock_prices = {
        "AAPL": 180,
        "TSLA": 250,
        "MSFT": 400,
        "GOOGL": 170,
        "AMZN": 150
    }
    
    display_available_stocks(stock_prices)
    
    number_of_stocks= int(input("Enter the different no. of stock you own: "))
    total = 0
    
    for _ in range(number_of_stocks):
        stock = get_valid_stock(stock_prices)
        total = calculate_portfolio(stock,stock_prices,total)

    print_summary(total)
    save_portfolio(total)


if __name__ == "__main__":
    main()