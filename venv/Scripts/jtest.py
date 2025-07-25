import yfinance as yf

samsung = yf.download('005930.KS', period='5y')
print(samsung.head())