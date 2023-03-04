import fundy.prices as pd
from fundy.trade import open_lot, short_order


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
                triggered = False
                if predicate(ticker_prices):
                    triggered = True
                    break
            results.append(triggered)
        return results

    def run_actions(self):
        predicates = self.run_predicates()
        res = []
        for idx, predicate in enumerate(predicates):
            if predicate:
                action = open_lot if self.actions[idx][0] else short_order
                res.append(action(self.tickers[idx], self.actions[idx][1])['status'])
        return res


# x1 = lambda a : ind.consecutive(a['High'].tolist(), 5)
# x2 = lambda a : ind.dup_range(a, 5)
# x3 = lambda a : ind.hurst(a, 5)[1] < ind.hurst(a, 5)[2]


# s = Strategy('myStrat', ['AAPL', 'AAPL', 'AAPL'], [x1, x2, x3], [(True, 1), (True, 1), (True, 1)])
