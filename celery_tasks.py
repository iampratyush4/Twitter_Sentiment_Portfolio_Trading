from celery import Celery
from config import ALPACA_API_KEY, ALPACA_SECRET_KEY, REDIS_URL
from sentiment import sia, predict_sentiment
from alpaca_trade_api import REST

app = Celery('tasks', broker=REDIS_URL)
api = REST(ALPACA_API_KEY, ALPACA_SECRET_KEY, base_url='https://paper-api.alpaca.markets')

@app.task
def process_tweet(tweet_text):
    # Get sentiment scores
    vader_score = sia.polarity_scores(tweet_text)['compound']
    ml_score = predict_sentiment(tweet_text)  # 0=negative, 1=positive
    
    # Generate signal (simple hybrid approach)
    if vader_score > 0.5 and ml_score == 1:
        execute_trade('BUY', 'AAPL')  # Example: Buy Apple
    elif vader_score < -0.5 and ml_score == 0:
        execute_trade('SELL', 'AAPL')

def execute_trade(signal, symbol):
    # Get current position
    position = api.get_position(symbol)
    
    if signal == 'BUY' and not position:
        api.submit_order(symbol, qty=1, side='buy', type='market')
    elif signal == 'SELL' and position:
        api.submit_order(symbol, qty=1, side='sell', type='market')