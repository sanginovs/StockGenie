#Imports the library needed to send an
#http request to the API
from app import mainDB, models
import json
import requests

time = 'Time Series (Daily)'
close = '4. close'
openp = '1. open'
low = '3. low'
high = '2. high'
symbol = '2. Symbol'

chosenStocks = ['APPL', 'GOOGL']

#This is the api key we will be using
apiKey = "NOKRTCHWT6DAEHUY"
mainDB.begin()

#This requests data from the api
#This is an example request to get all the stock data
#They have on apple's stock
def connect(stockName):

    response = requests.get("https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=" + stockName + "&outputsize=full&apikey=" + apiKey)

    #Prints out the data received
    data = json.loads(response.text)
    return data

for stock in chosenStocks:
    print("Collecting data for " + stock)

    success = False
    data = {'Error Message':'Error'}
    while not success or data.keys()[0] == 'Error Message':
        success = False
        try:
            data = connect(stock)
            success = True
        except:
            print('Could not Connect. Trying again')
            pass
    print('Connection passed')
    dates = data[time].keys()
    print('Starting to Add to DB')
    for info in dates:
        symbols = data['Meta Data'][symbol]
        opens = data[time][info][openp]
        closes = data[time][info][close]
        highs = data[time][info][high]
        lows = data[time][info][low]
        models.StockData.create(open=opens,close=closes,high=highs,low=lows,date=info,symbol=symbols)
        mainDB.commit()
