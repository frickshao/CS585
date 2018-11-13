import json

with open("tweets.json", "r") as tweet_db:
    tweets = json.load(tweet_db)

def to_text(tweets):
    '''Converts from a list of tweets to a list of tweet contents and converts all text to lower case.
    The conversion to lowercase reduces how much the model has to learn
    Example Uses:
    tweet1 = {"content": "My hands are YUUGE!", ...}
    tweet2 = {"content": "#MAGA", ...}
    tweet3 = {"content": "I hate Little Marco.", ...}
    tweets = [tweet1, tweet2, tweet3]
    to_text(tweets) # => ["my hands are yuuge!", "#maga", "i hate little marco."]
    '''
    return list(x['text'].lower() for x in tweets)


lst = to_text(tweets)
print(lst)























