import websocket
import json
import requests
import finnhub
import time
import requests

class MarketData:
	def __init__(self,key):
		#API_KEY = 'me_8_6Tcpm4iG25tz_ZXKy0rEp4lFoYfwURXuP'
		self.API_KEY = key
		self.finnhub_client = self.establishConnection(self.API_KEY)
		#self.token = tk
		

	def establishConnection(self,key):
		return finnhub.Client(api_key=key)

	def getCurrentPrice(self,ticker):
		fr = int(time.time())
		to = fr + 60
		res = self.finnhub_client.stock_candles(ticker, 'D', fr, to)
		return res
	def gerRSI(self,ticker,indicator,timeperiod):
		fr = int(time.time())
		to = fr + 60
		token = 'bsa6sbvrh5rfukjh0gl0'
		r = requests.get('https://finnhub.io/api/v1/indicator?symbol='+ticker+'&resolution=D&from='+str(fr)+'&to='+str(to)+'&indicator='+indicator+'&timeperiod='+str(timeperiod)+'&token='+token)
		return r
	#return current, high, low
	def getQuote(self,ticker):
		dt = self.finnhub_client.quote(ticker)
		return dt['c'],dt['h'],dt['l']

    	#technical_analysis': {'count': {'buy': 10, 'neutral': 6, 'sell': 1},
        #'signal': 'buy'},
	def aggregrateIndicators(self,ticker):
		dt = self.finnhub_client.aggregate_indicator('AAPL', '1')
		return dt


