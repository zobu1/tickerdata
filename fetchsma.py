import yfinance as yf
import pandas as pd
import pandas_ta as ta
from datetime import datetime, timedelta

def get_sma(symbol , len):
    today = datetime.today()
    dif = timedelta(days = len)
    earlier = today - (2 * dif)
    earlier_str = earlier.strftime("%Y-%m-%d")
    
    today = datetime.today().strftime('%Y-%m-%d')
    data = yf.download(symbol , start = earlier_str, end = today)
    data = pd.concat([data, pd.DataFrame({'Close': [get_current_price(symbol)]})], ignore_index=True)

    sma = ta.sma(data["Close"] , length = len)
    data = data.assign(SMA = sma)
    price = data.iloc[-1]['SMA']
    return price

def get_current_price(symbol):
    ticker = yf.Ticker(symbol)
    todays_data = ticker.history(period='1d')
    return todays_data['Close'][0]


symbol = input("Enter Ticker \n")
symbol = symbol.upper()

len = int(input("Enter SMA length \n"))
print(get_sma(symbol , len))
