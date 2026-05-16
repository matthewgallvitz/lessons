import ccxt

exchange = ccxt.coinbase() # or binance(), coinbase(), kucoin(), etc.
# [ts, open, high, low, close, volume]
ohlcv = exchange.fetch_ohlcv('BTC/USD', '1d', limit=2)

print(ohlcv[1])
high = ohlcv[1][2]
low = ohlcv[1][3]
print (high)
print (low)