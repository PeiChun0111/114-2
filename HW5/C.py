import pandas as pd
import numpy as np

class StockTracker:
    def __init__(self, prices):
        # Convert list to Pandas Series
        self.prices = pd.Series(prices)

    def moving_average(self, window):
        # Calculate rolling mean
        ma = self.prices.rolling(window=window).mean()
        # Replace NaN with 0.0
        ma = ma.fillna(0.0)
        return ma

N, W = map(int, input().split())
prices = list(map(int, input().split()))

tracker = StockTracker(prices)
result = tracker.moving_average(W)

print(*[f"{x:.1f}" for x in result])