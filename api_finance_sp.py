##api_finance RAPID API site. Freemium 500 calls a month.
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime
import requests
from matplotlib import rcParams
#json is part the anaconda root enviornment. no need to download. 
import json

# Check the authentication and connection
url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/market/get-charts"

querystring = {"symbol":"AAPL"}

headers = {
    'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com",
    'x-rapidapi-key': "25eb8aceadmshfb3c2de6919d91fp1dfb74jsnc41ea485775c"
    }

response = requests.request("GET", url, headers=headers, params=querystring)
#status code for when checking to see if you get a correct response.
print(response.status_code)

parsedata = response.json()
print(len(parsedata))
parse_str = json.dumps(parsedata['chart']['result'][0], indent=2)
print(parse_str)

time_stamp = parsedata['chart']['result'][0]['timestamp']

calendartime= []
for ts in time_stamp:
    dt = datetime.fromtimestamp(ts)
    calendartime.append(dt.strftime("%m/%d/%Y %r"))
print(calendartime)

#could make a function here.

def test():
    basic = parsedata["chart"]["result"][0]["indicators"]["quote"][0]
    return basic

stock_low = test()["low"]
stock_close = test()["close"]
stock_open = test()["open"]
stock_high = test()["high"]
stock_volume = test()["volume"]
#========================================================================================
#before i created the function i copied the parse data several times
# stock_low = parsedata["chart"]["result"][0]["indicators"]["quote"][0]["low"]
# stock_close = parsedata["chart"]["result"][0]["indicators"]["quote"][0]["close"]
# stock_open = parsedata["chart"]["result"][0]["indicators"]["quote"][0]["open"]
# stock_high = parsedata["chart"]["result"][0]["indicators"]["quote"][0]["high"]
# stock_volume = parsedata["chart"]["result"][0]["indicators"]["quote"][0]["volume"]
#========================================================================================

#will test here...
my_dict = {'Time': calendartime,
'Low': stock_low,
'Close': stock_close,
'Open' : stock_open,
'High' : stock_high,
'Volume': stock_volume
}

all_info = pd.DataFrame(my_dict)

print(all_info)
#print(response.body)
#print(response.text)