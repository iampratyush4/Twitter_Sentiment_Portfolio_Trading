import backtrader as bt
import yfinance as yf
from sentiment import predict_sentiment  # Reuse sentiment model

class SentimentStrategy(bt.Strategy):
    def __init__(self):
        self.sma = bt.indicators.SMA(period=20)
        self.sentiments = []

    def next(self):
        # Get sentiment for current day's news (mock implementation)
        sentiment = predict_sentiment("Dummy text")  # Replace with historical tweet data
        if sentiment == 1 and self.data.close[0] > self.sma[0]:
            self.buy()
        elif sentiment == 0 and self.data.close[0] < self.sma[0]:
            self.sell()

# Run backtest
data = bt.feeds.PandasData(dataname=yf.download('AAPL', '2020-01-01', '2023-01-01'))
cerebro = bt.Cerebro()
cerebro.adddata(data)
cerebro.addstrategy(SentimentStrategy)
results = cerebro.run()
print(f"Final Portfolio Value: {cerebro.broker.getvalue():.2f}")