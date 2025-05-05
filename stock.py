import yfinance as yf

class StockPortfolio:
    def _init_(self):
        self.stocks = {}

    def add_stock(self, symbol, shares):
        if symbol in self.stocks:
            self.stocks[symbol] += shares
        else:
            self.stocks[symbol] = shares
        print(f"Added {shares} shares of {symbol}")

    def remove_stock(self, symbol, shares):
        if symbol in self.stocks:
            if shares >= self.stocks[symbol]:
                del self.stocks[symbol]
                print(f"Removed all shares of {symbol}")
            else:
                self.stocks[symbol] -= shares
                print(f"Removed {shares} shares of {symbol}")
        else:
            print(f"No shares of {symbol} found in portfolio.")

    def get_portfolio_value(self):
        total_value = 0
        print("\nCurrent Portfolio:")
        for symbol, shares in self.stocks.items():
            stock = yf.Ticker(symbol)
            price = stock.history(period="1d")['Close'][0]
            value = price * shares
            total_value += value
            print(f"{symbol}: {shares} shares x ${price:.2f} = ${value:.2f}")
        print(f"\nTotal Portfolio Value: ${total_value:.2f}")
        return total_value

def main():
    portfolio = StockPortfolio()

    while True:
        print("\nOptions: 1. Add Stock  2. Remove Stock  3. View Portfolio  4. Exit")
        choice = input("Choose an option (1-4): ")

        if choice == '1':
            symbol = input("Enter stock symbol: ").upper()
            shares = int(input("Enter number of shares: "))
            portfolio.add_stock(symbol, shares)
        elif choice == '2':
            symbol = input("Enter stock symbol: ").upper()
            shares = int(input("Enter number of shares to remove: "))
            portfolio.remove_stock(symbol, shares)
        elif choice == '3':
            portfolio.get_portfolio_value()
        elif choice == '4':
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__== "_main_":main()