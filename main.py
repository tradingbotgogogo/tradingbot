import websocket
import json
import requests
import finnhub
import time
import requests
from MarketInfo import MarketData
from webhook import StreamData

if __name__ == "__main__":
	API_KEY = 'bshp9jvrh5r8b9vl3d70'
	webhook = "bshp98frh5r8b9vl3cs0"
	MI = MarketData(API_KEY)
	print("ger current price")
	print(MI.getCurrentPrice("AAPL"))
	print("RSI")
	print(MI.gerRSI("AAPL",'rsi',4))
	print("quote")
	print(MI.getQuote("AAPL"))
	print("indicators")
	print(MI.aggregrateIndicators("AAPL"))
	sd = StreamData(API_KEY)
	sd.stream_on_ticker("AAPL")


    # websocket.enableTrace(True)
    # ws = websocket.WebSocketApp("wss://ws.finnhub.io?token=bsa6sbvrh5rfukjh0gl0",
    #                           on_message = on_message,
    #                           on_error = on_error,
    #                           on_close = on_close)
    # ws.on_open = on_open
    # ws.run_forever()