# We import pandas into Python
import pandas as pd

google_stock = pd.read_csv(r'learn_python\pandas\statistics_from_stock_data\GOOG.csv', index_col=['Date'], usecols=['Date', 'Adj Close'], parse_dates=True)
apple_stock = pd.read_csv(r'learn_python\pandas\statistics_from_stock_data\AAPL.csv', index_col=['Date'], usecols=['Date', 'Adj Close'], parse_dates=True)
amazon_stock = pd.read_csv(r'learn_python\pandas\statistics_from_stock_data\AMZN.csv', index_col=['Date'], usecols=['Date', 'Adj Close'], parse_dates=True)

# We create calendar dates between '2000-01-01' and  '2016-12-31'
dates = pd.date_range('2004-08-19', '2016-12-31')

# We create and empty DataFrame that uses the above dates as indices
all_stocks = pd.DataFrame(index = dates)


# Change the Adj Close column label to Google
google_stock = google_stock.rename(columns = {'Adj Close' : 'Google'})
#print(google_stock.head())

# Change the Adj Close column label to Apple
apple_stock = apple_stock.rename(columns = {'Adj Close' : 'Apple'})
#print(all_stocks.head())

# Change the Adj Close column label to Amazon
amazon_stock = amazon_stock.rename(columns = {'Adj Close' : 'Amazon'})

# We join the Google stock to all_stocks
all_stocks = all_stocks.join(google_stock)

# We join the Apple stock to all_stocks
all_stocks = all_stocks.join(apple_stock)

# We join the Amazon stock to all_stocks
all_stocks = all_stocks.join(amazon_stock)

print(all_stocks.head())
