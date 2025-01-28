import tweepy
from config import REDIS_URL, TWITTER_BEARER_TOKEN
import redis

# Connect to Redis
redis_client = redis.from_url(REDIS_URL)

class TweetStream(tweepy.StreamingClient):
    def on_tweet(self, tweet):
        if tweet.text:
            redis_client.publish('tweets', tweet.text)

# Start stream
stream = TweetStream(bearer_token=TWITTER_BEARER_TOKEN)
stream.add_rules(tweepy.StreamRule("$SPY OR $AAPL OR $BTC"))  # Track these symbols
stream.filter()