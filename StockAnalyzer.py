import yfinance as yf
import pandas as pd
import pandas_ta as ta
from datetime import datetime, timedelta

class StockAnalyzer:
    def __init__(self, symbol):
        self.symbol = symbol.upper()
        self.ticker = yf.Ticker(self.symbol)

    def get_time(self, len):
        today = datetime.today()
        dif = timedelta(days=len)
        earlier = today - (2 * dif)
        return earlier.strftime("%Y-%m-%d")

    def get_data(self, len):
        today = datetime.today().strftime('%Y-%m-%d')
        data = yf.download(self.symbol, start=self.get_time(len), end=today)
        data = pd.concat([data, pd.DataFrame({'Open': [self.get_open_price()], 'Close': [self.get_current_price()]})], ignore_index=True)
        return data

    def get_current_price(self):
        todays_data = self.ticker.history(period='1d')
        return todays_data['Close'][0]

    def get_open_price(self):
        todays_data = self.ticker.history(period='1d')
        return todays_data['Open'][0]

    def get_sma(self, len):
        data = self.get_data(len)
        sma = ta.sma(data["Close"], length=len)
        data = data.assign(SMA = sma)
        return data.iloc[-1]['SMA']
    
    def get_ema(self, len):
        data = self.get_data(len)
        ema = ta.ema(data["Close"], length=len)
        data = data.assign(EMA = ema)
        return data.iloc[-1]['EMA']

    def get_rsi(self, len):
        data = self.get_data(len)
        rsi = ta.rsi(data["Close"], length=len)
        data = data.assign(RSI = rsi)
        return data.iloc[-1]['RSI']

    def get_stdev(self, len):
        data = self.get_data(len)
        stdev = ta.stdev(data["Close"], length=len)
        data = data.assign(STDEV = stdev)
        return data.iloc[-1]['STDEV']

    def get_cumr(self, len):
        data = self.get_data(len)
        length = data.shape[0] - 1 # Get index of last row
        cumrp = (self.get_current_price() / data.loc[length - (len - 1), 'Close'])
        return cumrp
    
    def get_adr(self , len): # Return Average Dollar Volume over len days in millions
        data = self.get_data(len)
        length = data.shape[0] - 1 # Get index of last row
        first = length - len # Get first value
        total = 0
        for i in range (first , length):
            total += data.loc[i , 'Close'] * data.loc[i , 'Volume']
        return (total / len) / 1000000

def main():
    symbol = input("Enter Ticker \n")
    analyze = StockAnalyzer(symbol)
    #print(analyze.get_data(5))

    signal = input("0. Exit \n1. SMA \n2. EMA \n2. RSI \n3. STDEV \n4. CUMR\n5. ADR\n")
    if signal == "0":
        quit()
    else:
        len = int(input("Enter length \n"))
        if signal == "1":
            print(analyze.get_sma(len))
        elif signal == "2":
            print(analyze.get_ema(len))
        elif signal == "3":
            print(analyze.get_rsi(len))
        elif signal == "4":
            print(analyze.get_stdev(len))
        elif signal == "5":
            print(analyze.get_cumr(len))
        elif signal == "6":
            print(analyze.get_adr(len))

if __name__ == "__main__":
    main()
