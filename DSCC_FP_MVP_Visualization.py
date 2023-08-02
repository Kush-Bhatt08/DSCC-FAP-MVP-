import matplotlib.pyplot as plt

def visualize_data(stock_data, symbol):
    """
    Visualizes the stock data.
    """
    symbol = "APPLE" if str.lower(symbol).strip() == 'aapl' else "SAMSUNG"
    plt.plot(stock_data['Close'])
    plt.xlabel('Date')
    plt.ylabel('Closing Price')
    plt.title('Stock Data ' + symbol)
    plt.show()