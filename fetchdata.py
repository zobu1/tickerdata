import yfinance as yf

stock = input("Enter Ticker \n")
stock = stock.upper()

print("Format: XXXX-XX-XX")
start_date = input("Start Date \n")
end_date = input ("End Data \n")
period_input = input ("Period \n")

data = yf.download(stock , start = start_date , end = end_date , period = period_input)
data.to_csv(stock + ".csv")

