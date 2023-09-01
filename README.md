# Fetch Data
- This is a simple script to grab data for any stock. 
- Data retrieved using YahooFinance's API
- Periods: "1m" , "1h" , "1d" , "1wk" , "1mo" 
- For periods of 1m, data may only be fetched from the last 7 days.
- Less than 1d, past 60 days.
- Data is outputted to CSV.
# Fetch SMA
- Grab SMA for n days
# StockAnalyzer
- Combination of all the individual scripts in this repo
- Fetch DAILY data for any stock
- Input ticker and length, and outputs real time stats
# StockAnalyzerStatic
- Uses static methods instead of creating an object for each ticker
