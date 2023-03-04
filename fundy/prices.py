import pandas as pd
import time
import datetime

TICKER_PRICES_BASE_URL = (
    'https://query1.finance.yahoo.com/v7/finance/download/{}?period1=1560172610&period2={}&interval=1d&events=history'
)


def get_stock_prices(ticker):
    currentDate = datetime.datetime.now()
    todayTimeStamp = int(time.mktime(currentDate.timetuple()))
    ticker_prices = pd.read_csv(TICKER_PRICES_BASE_URL.format(ticker, todayTimeStamp))
    return ticker_prices


def get_prices(tickers):
    prices = []
    for ticker in tickers:
        prices.append(get_stock_prices(ticker))
    return prices
