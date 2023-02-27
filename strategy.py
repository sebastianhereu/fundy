import indicators as ind
import prices as pd

class Strategy:
        def __init__(self, name, tickers, predicates, actions) -> None:
                self.name = name
                self.tickers = tickers
                self.predicates = predicates
                self.actions = actions
                
        def run_predicates(self):
                tickers = pd.get_prices(self.tickers)
                results = []
                for ticker_prices in tickers: 
                        for idx, predicate in enumerate(self.predicates):
                                if predicate(ticker_prices):
                                        results.append(True)
                                else:
                                        results.append(False)
                return results


# x1 = lambda a : ind.consecutive(a['High'].tolist(), 5)
# x2 = lambda a : ind.dup_range(a, 5)
# x3 = lambda a : ind.hurst(a, 5)[1] < ind.hurst(a, 5)[2]


# s = Strategy('myStrat', ['AAPL'], [x1, x2, x3])

# print(s.run_predicates())



                




