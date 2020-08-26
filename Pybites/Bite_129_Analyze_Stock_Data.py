import requests
from collections import Counter

STOCK_DATA = 'https://bites-data.s3.us-east-2.amazonaws.com/stocks.json'

# pre-work: load JSON data into program

with requests.Session() as s:
    data = s.get(STOCK_DATA).json()

def _cap_str_to_mln_float(cap):
    """If cap = 'n/a' return 0, else:
       - strip off leading '$',
       - if 'M' in cap value, strip it off and return value as float,
       - if 'B', strip it off and multiple by 1,000 and return
         value as float"""
    cap = cap.lstrip('$')
    if cap == 'n/a':
        return 0
    if 'M' in cap:
        return float(cap.replace('M', ''))
    if 'B' in cap:
        return float(cap.replace('B', '')) * 1000

def get_industry_cap(industry):
    """Return the sum of all cap values for given industry, use
       the _cap_str_to_mln_float to parse the cap values,
       return a float with 2 digit precision"""
    ret = sum(_cap_str_to_mln_float(line["cap"])
              for line in data if line["industry"] == industry)
    return round(ret, 2)

def get_stock_symbol_with_highest_cap():
    """Return the stock symbol (e.g. PACD) with the highest cap, use
       the _cap_str_to_mln_float to parse the cap values"""
    stocks_sorted = sorted(data, key=lambda x: _cap_str_to_mln_float(x["cap"]))
    return stocks_sorted[-1]['symbol']

def get_sectors_with_max_and_min_stocks():
    """Return a tuple of the sectors with most and least stocks,
       discard n/a"""
    cnt = Counter([x["sector"] for x in data
                   if x["sector"] != 'n/a']).most_common()
    return cnt[0][0], cnt[-1][0]

    # sectors = Counter(k['sector']
    #                   for k in data
    #                   if k.get('sector'))
    #
    # minimum = min(sectors, key=sectors.get)
    # maximum = sectors.most_common(2)[-1][0]
    # return (maximum, minimum)
