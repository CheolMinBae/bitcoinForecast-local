#!/usr/bin/python3

##
## run the code for about 2/3 days
##

# coin id
'''
https://api.coinmarketcap.com/v1/ticker/
ethereum
ripple
bitcoin-cash
litecoin
eos
tether
binance-coin
stellar
cardano
tron
monero
bitcoin-sv
dash
iota
cosmos

'''

import requests
import time

f_name = input("dataset name:")
f = open(f_name,"a")
keys = ["price_usd","24h_volume_usd","market_cap_usd","available_supply","total_supply","percent_change_1h","percent_change_24h","percent_change_7d"]
vals = [0]*len(keys)

while True:
  print('start collect')
  data = requests.get("https://api.coinmarketcap.com/v1/ticker/ethereum/").json()[0]
  bstamp = requests.get("https://www.bitstamp.net/api/v2/ticker/ethusd/").json()
  bkc = requests.get("https://blockchain.info/ticker").json()

  for d in data.keys():
     if d in keys:
       indx = keys.index(d)
       vals[indx] = data[d]
  for val in vals:
       f.write(val+",")

  f.write("{},{},".format(bstamp["volume"],bstamp["vwap"]))
  f.write("{},{},{}".format(bstamp["ask"],bstamp["bid"],bstamp["open"]))
  f.write("\n")
  f.flush()
  time.sleep(9*60)
