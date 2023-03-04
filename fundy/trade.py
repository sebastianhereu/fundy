import requests
import json
import numpy as np
from fundy.api_config import BASE_URL, SECRET_KEY, API_KEY_ID

ACCOUNT_URL = "{}/v2/account".format(BASE_URL)
ORDERS_URL = "{}/v2/orders".format(BASE_URL)
HEADERS = {'APCA-API-KEY-ID': API_KEY_ID, 'APCA-API-SECRET-KEY': SECRET_KEY}
OPEN_POSITIONS_URL = "{}/v2/positions".format(BASE_URL)


def get_account():
    r = requests.get(ACCOUNT_URL, headers=HEADERS)

    return json.loads(r.content)


def create_order(symbol, qty, side, type, time_in_force, limit_price):

    if limit_price != 0:
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

    r = requests.post(ORDERS_URL, json=data, headers=HEADERS)

    print(json.loads(r.content))
    return json.loads(r.content)


def get_open_orders():

    tickerData = []

    data = json.loads(requests.get(ORDERS_URL, headers=HEADERS).content)

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

    try:
        r = create_order(ticker, size, "buy", "market", "day", 0)
        return r
    except Exception as e:
        raise Exception("order failed!: ", e.message)


def short_order(ticker, size):

    try:
        r = create_order(ticker, size, "sell", "market", "day", 0)
        return r
    except Exception as e:
        raise Exception("order failed!: ", e.message)


def open_lot(symbol, size):

    lotID = np.random.randint(low=1, high=1000000000, size=1)[-1]

    if size > 0:
        order = long_order(symbol, abs(size)) if size > 0 else short_order(symbol, abs(size))
        date = str(order['submitted_at'])
        p = str(order['filled_avg_price'])
        # p = '45'

        with open('trade-data.txt', 'a') as file:
            file.write(
                date
                + '/'
                + symbol
                + '/'
                + p
                + '/'
                + str(size)
                + '/'
                + ('long' if size > 0 else 'short')
                + '/'
                + str(lotID)
            )
            file.write('\n')
            file.close()
        return order


def close_lot(prices, symbol, size, LotID):

    #     p = str(prices[index][-1])
    p = '45'

    if size > 0:

        date = str(long_order(symbol, abs(size)))

        with open('outputs/trade-data-closes.txt', 'a') as file:
            file.write(date + '/' + symbol + '/' + p + '/' + str(size) + '/' + 'long' + '/' + str(int(LotID)))
            file.write('\n')
            file.close()
    else:
        date = short_order(symbol, abs(size))

        with open('trade-data-closes.txt', 'a') as file:
            file.write(date + '/' + symbol + '/' + p + '/' + str(size) + '/' + 'short' + '/' + str(int(LotID)))
            file.write('\n')
            file.close()
