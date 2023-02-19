import requests
import json
import numpy as np
from api_config import *

ACCOUNT_URL = "{}/v2/account".format(BASE_URL)
ORDERS_URL = "{}/v2/orders".format(BASE_URL)
HEADERS = {'APCA-API-KEY-ID': API_KEY_ID , 'APCA-API-SECRET-KEY': SECRET_KEY}
OPEN_POSITIONS_URL = "{}/v2/positions".format(BASE_URL)

def get_account():
    r = requests.get(ACCOUNT_URL, headers = HEADERS)

    return json.loads(r.content)


def create_order(symbol, qty, side, type, time_in_force , limit_price):


    if(limit_price != 0):
        data = {
            "symbol": symbol,
            "qty": qty,
            "side": side,
            "type": type,
            "time_in_force": time_in_force,
            "limit_price": limit_price,

        }
    else:
         data = {
            "symbol": symbol,
            "qty": qty,
            "side": side,
            "type": type,
            "time_in_force": time_in_force,

        }


    r = requests.post(ORDERS_URL, json=data ,headers = HEADERS)

    print(json.loads(r.content))
    return json.loads(r.content)

def get_open_orders():

    tickerData = []
    
    data = json.loads(requests.get(ORDERS_URL, headers= HEADERS).content)

    for i in range(len(data)):
        
        tickerData.append(data[i]['symbol'])

    return tickerData


def get_open_positions():

    tickerData = []
    
    data = json.loads(requests.get(OPEN_POSITIONS_URL, headers=HEADERS).content)


    for i in range(len(data)):
        
        tickerData.append(data[i]['symbol'])

    return tickerData



def long_order(ticker, size):
    r = create_order(ticker, size, "buy", "market", "day", 0)
    
    try:
        return r['submitted_at']
    except:
        return 'ERROR'

def short_order(ticker, size):
    r = create_order(ticker, size, "sell", "market", "day", 0)
    try:
        return r['submitted_at']
    except:
        return 'ERROR'
   

def open_lot(prices ,symbol, size, index, signal, variables):
    
    p = str(prices[index][-1])

    lotID = np.random.randint(low=1, high=1000000000, size=1)[-1]
    
    if(size>0):
        
        date = str(long_order(symbol, abs(size) ) )
        
        with open('trade-data.txt', 'a') as file:
            file.write(date + '/' + symbol + '/' + p + '/' + str(size) + '/' + 'long' + '/' + signal + '/' + str(variables[0]) + '/' + str(variables[1]) + '/' + str(variables[2]) + '/' +str(variables[3]) +'/' + str(variables[4]) +'/' + str(lotID))
            file.write('\n')
            file.close()
    else:
        date = str(short_order(symbol, abs(size) ) )

        with open('trade-data.txt', 'a') as file:
            file.write(date + '/' + symbol + '/' + p + '/' + str(size) + '/' + 'short' + '/' + signal + '/' + str(variables[0]) + '/' + str(variables[1]) + '/' + str(variables[2]) + '/' +str(variables[3]) +'/' + str(variables[4])+'/' + str(lotID) )
            file.write('\n')
            file.close()

def close_lot(prices ,symbol,size, index, LotID):

    p = str(prices[index][-1])
    
    if(size>0):

        date = str(long_order(symbol, abs(size)))

        with open('trade-data-closes.txt', 'a') as file:
            file.write(date + '/' + symbol + '/' + p + '/' + str(size) + '/' + 'long' + '/' + str(int(LotID)))
            file.write('\n')
            file.close()
    else:
        date = short_order(symbol, abs(size))

        with open('trade-data-closes.txt', 'a') as file:
            file.write(date + '/' + symbol + '/' + p + '/' + str(size) + '/' + 'short' + '/' + str(int(LotID)))
            file.write('\n')
            file.close()


