
# https://github.com/mehranshakarami/AI_Spectrum/blob/main/2022/snscrape/tweets.py

import snscrape.modules.twitter as sntwitter
import pandas as pd

# query = "(from:elonmusk) until:2020-01-01 since:2010-01-01"
query = "ronaldo lang:en until:2022-12-20 since:2022-11-1"
tweets = []
limit = 5000


for tweet in sntwitter.TwitterSearchScraper(query).get_items():
    
    # print(vars(tweet))
    # break
    if len(tweets) == limit:
        break
    else:
        # tweets.append([tweet.date, tweet.user.username, tweet.content])
        tweets.append([tweet.content])
        
df = pd.DataFrame(tweets, columns=['Tweet'])
print(df)

# to save to csv
df.to_csv('tweets_ronaldo.csv')