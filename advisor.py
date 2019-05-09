import requests
from dotenv import load_dotenv

import csv
import json
import os
import datetime



def to_usd(my_price):
  return "${0:,.2f}".format(my_price)



load_dotenv()  #loads environment variables set in a ".env" file, including the value of the ALPHAVANTAGE_API_KEY variable

def compile_url(symbol):
  symbol = input("please state symbol")
  api_key = os.environ.get("ALPHAVANTAGE_API_KEY") # see: https://www.alphavantage.co/support/#api-key
  request_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={api_key}"
  

def get_response(symbol):
  request_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={api_key}"
  response = requests.get(request_url)
  parsed_response = json.loads(response.text)
  return parsed_response

def float_conversion(x):
  float(x)


table_rows =[]
def decipher_response(parsed_response):
  tsd = parsed_response["Time Series (Daily)"] #short for time series daily
  for date, daily_prices in tsd.items():
    row = {
        "timestamp": date,
        "open": float(daily_prices["1. open"]),
        "high": float(daily_prices["2. high"]),
        "low": float(daily_prices["3. low"]),
        "close": float(daily_prices["4. close"]),
        "volume": int(daily_prices["5. volume"])
    }
    table_rows.append(row)
  return table_rows
  


def write_to_csv(rows,csv_filepath):

  csv_headers = ["timestamp", "open", "high", "low", "close", "volume"] #list of dictionaries
  
  with open(csv_filepath, "w") as csv_file:  # "w" means "open the file for writing"
      writer = csv.DictWriter(csv_file, fieldnames=csv_headers)
      writer.writeheader()  # uses fieldnames set above
      for row in table_rows:
        writer.writerow(row)

  return True

if __name__ == "__main__":
  #INPUTS
  now = datetime.datetime.now()
  symbol = input("please input symbol")
  parsed_response = get_response(symbol)# TODO: further parse the JSON response...

  last_refreshed = parsed_response["Meta Data"]["3. Last Refreshed"]
  table_rows = decipher_response(parsed_response)

  latest_price = table_rows[0]["close"]
  high_prices =[row["high"] for row in table_rows]
  low_prices =[row["low"] for row in table_rows]
  recent_high =max(high_prices)
  recent_low =min(low_prices)
  #OUTPUTS
  csv_filepath = os.path.join(os.path.dirname(__file__), "..", "revisit-advisor", "prices4.csv") # TODO: write response data to a CSV file #csv_file_path = "data/prices.csv"  # a relative filepath
  write_to_csv(table_rows,csv_filepath)

  format_time =now.strftime("%Y-%m-%d %H:%M:%S")
  formatted_csv_filepath = csv_filepath.split("../")[1]


# TODO: further revise the example outputs below to reflect real information
  print("-------------------------")
  print(f"SYMBOL: {symbol}")
  print("-------------------------")
  print(f"REQUEST AT: {format_time}")
  print(f"REFRESH DATE: {last_refreshed}")
  print("-------------------------")
  print(f"RECENT HIGH:  {to_usd(recent_high)}")
  print(f"LATEST CLOSE: {to_usd(latest_price)}")
  print(f"RECENT LOW:   {to_usd(recent_low)}")
  print("-------------------------")
  print("RECOMMENDATION: Buy the stock") # TODO
  print("BECAUSE: the stock will continue growing & has great market power!") 
  print(f"WRITING DATA TO CSV: {formatted_csv_filepath}")
  print("-------------------------")
  print("HAPPY INVESTING!")
  print("-------------------------")