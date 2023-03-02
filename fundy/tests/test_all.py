from fundy import (
    hello,
    print_hello,
    get_stock_prices,
    get_prices,
    consecutive,
    create_order,
    open_lot,
    Strategy,
    get_open_positions,
)
from unittest.mock import patch
from numpy import random

TEST_TICKERS = ['AAPL', 'TSLA', 'AXP']


def test_hello():
    assert hello() == "Hello, world!"


@patch('builtins.print')
def test_print_hello(mock_print):
    print_hello()
    assert mock_print.call_args.args == ("Hello, world!",)


def test_get_stock_prices():
    assert get_stock_prices(TEST_TICKERS[0])['Open'][0] > 0


def test_get_prices():
    price_data = get_prices(TEST_TICKERS)
    assert len(price_data) == len(TEST_TICKERS)
    for ticker in price_data:
        assert ticker['Open'][0] > 0


def test_consecutive():
    ascending_data = sorted((random.rand(1000) * 1000).tolist())
    assert consecutive(ascending_data, 999)
    ascending_data.reverse()
    assert consecutive(ascending_data, 999, True)


def test_create_order():
    response = create_order(TEST_TICKERS[0], 1, 'buy', 'market', 'gtc', 0)
    assert response['id']


def test_open_lot():
    open_lot(TEST_TICKERS[0], 1)
    with open('trade-data.txt', 'r') as f:
        for ln in f:
            pass
        last_line = ln
        f.close()
    written = last_line.split('/')
    assert written[1] == TEST_TICKERS[0]


def x1(a):
    return False


def x2(a):
    return False


def x3(a):
    return True


def x4(a):
    return False


def test_run_predicates():
    true_strat = Strategy('myStrat', [TEST_TICKERS[0]], [x1, x2, x3], [(True, 1), (True, 1), (True, 1)])
    false_strat = Strategy('myStrat', [TEST_TICKERS[0]], [x1, x2, x4], [(True, 1), (True, 1), (True, 1)])
    true_pred = true_strat.run_predicates()[0]
    false_pred = false_strat.run_predicates()[0]
    assert true_pred and (not false_pred)


# Integration test - uses trade module AND Strategy object's run_predicates
def test_run_actions():
    strat = Strategy(
        'myStrat', [TEST_TICKERS[0], TEST_TICKERS[0], TEST_TICKERS[0]], [x3, x3, x3], [(True, 1), (True, 1), (True, 1)]
    )
    statuses = strat.run_actions()
    assert len(statuses) == 3
