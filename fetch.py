import yfinance as yf
import pandas as pd
import pandas_ta as ta
from datetime import datetime, timedelta

def get_time(len):
    today = datetime.today()
    dif = timedelta(days = len)
    earlier = today - (2 * dif)
    earlier_str = earlier.strftime("%Y-%m-%d")
    return earlier_str

def get_current_price(symbol):
    ticker = yf.Ticker(symbol)
    todays_data = ticker.history(period='1d')
    return todays_data['Close'][0]

def get_open_price(symbol):
    ticker = yf.Ticker(symbol)
    todays_data = ticker.history(period='1d')
    return todays_data['Open'][0]

def get_data(symbol , len):
    today = datetime.today().strftime('%Y-%m-%d')
    data = yf.download(symbol , start = get_time(len), end = today)
    data = pd.concat([data, pd.DataFrame({'Open': [get_open_price(symbol)], 'Close': [get_current_price(symbol)]})], ignore_index=True)
    return data


def get_sma(symbol , len):
    data = get_data(symbol , len)
    sma = ta.sma(data["Close"] , length = len)
    data = data.assign(SMA = sma)
    value = data.iloc[-1]['SMA']
    return value

def get_rsi(symbol , len):
    data = get_data(symbol , len)
    rsi = ta.rsi(data["Close"] , length = len)
    data = data.assign(RSI = rsi)
    value = data.iloc[-1]['RSI']
    return value


symbol = input("Enter Ticker \n")
symbol = symbol.upper()



len = int(input("Enter SMA length \n"))
print(get_sma(symbol , len))
