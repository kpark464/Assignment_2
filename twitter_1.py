from twython import Twython
import pprint

# Replace the following strings with your own keys and secrets
TOKEN = "18197007-ErAniMa2itVxkEgFTm9F9YT9dFa8NYRa2gRiSqcbb"
TOKEN_SECRET = "0Eff2bqHywXoaaNQX4ZrpdcXSZxgvEkJJGXtRzCI0YIrz"
CONSUMER_KEY = "cWcX5RWLQD1KDcCh3pldieWyZ"
CONSUMER_SECRET = "LJMlx7Vu2JR1Fu5aKd4PymA6zGlnqfJsu6tsqF5kGVm9RDxeTc"


t = Twython(CONSUMER_KEY, CONSUMER_SECRET, TOKEN, TOKEN_SECRET)

data = t.show_user(screen_name="realdonaldtrump")
results = t.cursor(
    t.search, q="#WhatIDoNow", result_type="recent", count=25, tweet_mode="extended"
)
pprint.pprint(data)

for status in data["statuses"]:
    print(status["text"])
