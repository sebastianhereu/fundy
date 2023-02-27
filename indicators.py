import pandas as pd
import prices as pr
import numpy as np
import datetime
import talib


def consecutive(prices, length, loss=False):
        last_prices = prices[-(length):]  
        for idx in range(len((last_prices)) -1):
                safe = last_prices[idx] > last_prices[idx+1] if loss else last_prices[idx] < last_prices[idx + 1]
                if safe:
                        continue
                return False
        return True

def dup_range(priceframe, length, down=False, below=False):

        h = priceframe['High'].tolist()
        l = priceframe['Low'].tolist()
        c = priceframe['Close'].tolist()
        
        hrange = h[-1] < h[-(length+1)] if down else h[-1] > h[-(length+1)]
        crange =  c[-1] < c[-(length+1)] if below else c[-1] > c[-(length+1)]

        return hrange and crange


def super_smoother(index):

    p = close[index]

    return talib.TEMA(np.array(p), timeperiod=5)
    

def avg_true_range(priceframe, length):
        h = priceframe['High']
        l = priceframe['Low']
        c = priceframe['Close']     

        return talib.ATR(np.array(h), np.array(l) ,np.array(c) , timeperiod= length)
 

def rsi(priceframe, length , close=False):
        o = priceframe['Open']
        c = priceframe['Close']     

        if close: 
            
            return talib.RSI(np.array(c), timeperiod = length)

        else:

            return talib.RSI(np.array(o), timeperiod = length)


def hurst(priceframe, length):

        hursts = []
        h = priceframe['High']
        l = priceframe['Low']
        c = priceframe['Close']     

        for j in range(25,0,-1):

                if (length != 1):

                        hursts.append(np.log(  max(h[0:length]) - max(l[0:length]) ) - np.log(avg_true_range(priceframe, length)[-j]) /np.log(length))
        
        return hursts

def average(prices, length, *args):

    return talib.SMA(np.array(prices), timeperiod = length)


def ranges(priceframe, length):

        h = priceframe['High']
        l = priceframe['Low']
        
        ranges = []
        for i in range(length,0,-1):

                h = h[-i]
                l = l[-i]
                ranges.append(h - l)

        return ranges

def rate_of_change(length, index):

    c = close[index]
    
    return talib.ROC(np.array(c), timeperiod = length)


