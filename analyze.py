#!/usr/bin/env python3
from functools import *
import json
from copy import deepcopy
from operator import itemgetter
from statistics import *

with open("tweets.json", "r") as tweet_db:
    tweets = json.load(tweet_db)

# TODO: implement assigned functions

def flatten(xs):
    '''Flattens a list of lists to simply a list.
    Example Uses:
    flatten([[1, 2], [], [3, 4]]) # => [1, 2, 3, 4]
    '''
    return reduce(lambda x, y: x + y, xs)

def difference(xs, ys):
    '''Finds all the elements that are in either xs or ys , but not both.
    Example Uses:
    difference([1, 2], [2, 3]) # => [1, 3]
    '''
    return list(filter(lambda x: x not in ys, xs)) + \
           list(filter(lambda x: x not in xs, ys))

def to_text(tweets):
    '''Converts from a list of tweets to a list of tweet contents.
    Example Uses:
    tweet1 = {"content": "My hands are YUUGE!", ...}
    tweet2 = {"content": "#MAGA", ...}
    tweet3 = {"content": "I hate Little Marco.", ...}
    tweets = [tweet1, tweet2, tweet3]
    to_text(tweets) # => ["My hands are YUUGE!", "#MAGA", "I hate Little Marco."]
    '''
    return list(x['content'] for x in tweets)

def to_lowercase(tweets):
    '''Converts the content of each tweet in the list of tweets to lowercase.
    Example Uses:
    tweet1 = {"content": "My hands are YUUGE!", ...}
    tweet2 = {"content": "#MAGA", ...}
    tweet3 = {"content": "I hate Little Marco.", ...}
    tweets = [tweet1, tweet2, tweet3]
    to_text(to_lowercase(tweets))
    # => ["my hands are yuuge!", "#maga", "i hate little marco."]
    '''
    #return list(x['content'].lower() for x in tweets)
   # return lowercase_helper(deepcopy(tweets))
    return list(map(lambda tweet: lowercase_helper(tweet), deepcopy(tweets)))

def lowercase_helper(tweet):
    return {**tweet,**{'content': tweet['content'].lower()}}

def nonempty(tweets):
    '''Removes all tweets with empty contents from the list of tweets.
    Example Uses:
    tweet1 = {"content": "#MAGA", ...}
    tweet2 = {"content": "", ...}
    tweet3 = {"content": "#CrookedHillary", ...}
    tweets = [tweet1, tweet2, tweet3]
    to_text(nonempty(tweets)) # => ["#MAGA", "#CrookedHillary"]
    '''
    #return list(filter(lambda x: x != "", to_text(tweets)))
    #return list(map(lambda tweet: nonempty_helper(tweet), deepcopy(tweets)))
    return list(filter(lambda tweet: tweet['content'] != '', deepcopy(tweets)))

def total_word_count(tweets):
    ''' Calculates the total number of words in each tweet in a list.
    Example Uses:
    tweet1 = {"content": "I am President now.", ...}
    tweet2 = {"content": "Make America Safe Again!", ...}
    tweet3 = {"content": "Make America Great Again!", ...}
    tweets = [tweet1, tweet2, tweet3]
    total_word_count(tweets) # => 12
    '''
    return len(words_as_list(tweets))

def words_as_list(tweets):
    return flatten((list(x+ ' ' for x in to_text(nonempty(tweets))))).split()

def hashtags(tweet):
    '''Gets a list of all the hashtags from the specified tweet.
    Example Uses:
    tweet = {"content": "Hello, America. #MAGA #Trump2016", ...}
    hashtags(tweet) # => ["#MAGA", "#Trump2016"]
    '''
    return list(filter(lambda x: '#' in x, tweet['content'].split()))

def mentions(tweet):
    '''– Gets a list of all the mentions from the specified tweet.
    Example Uses:
    tweet = {"content": "@aatxe would be a better president than me.", ...}
    mentions(tweet) # => ["@aatxe"]
    '''
    return list(filter(lambda x: '@' in x, tweet['content'].split()))

def all_hashtags(tweets):
    '''Returns a list of all hashtags from a list of tweets.
    Example Uses:
    tweet1 = {"content": "Hello, America. #MAGA #Trump2016", ...}
    tweet2 = {"content": "Lock her up! #CrookedHillary #MAGA", ...}
    tweet3 = {"content": "No hashtags in here.", ...}
    tweets = [tweet1, tweet2, tweet3]
    all_hashtags(tweets) # => ["#MAGA", "#Trump2016", "#CrookedHillary", "#MAGA"]
    '''
    return reduce(lambda x, y: x + y, (list(hashtags(x) for x in tweets)))

def all_mentions(tweets):
    '''Returns a list of all mentions from a list of tweets.
    Example Uses:
    tweet1 = {"content": "@cnn is fake news!", ...}
    tweet2 = {"content": "Can’t believe how many people buy @cnn fake news!", ...}
    tweet3 = {"content": "@marcorubio and I are friends now!", ...}
    tweets = [tweet1, tweet2, tweet3]
    all_mentions(tweets) # => ["@cnn", "@cnn", "@marcorubio"]
    '''
    return reduce(lambda x, y: x + y, (list(mentions(x) for x in tweets)))

def all_caps_tweets(tweets):
    '''Returns a list of all tweets that are completely capitalized from
    the given list of tweets.
    Example Uses:
    tweet1 = {"content": "MAKE AMERICA SAFE AGAIN!", ...}
    tweet2 = {"content": "Can’t believe how many people buy @cnn fake news!", ...}
    tweet3 = {"content": "AMERICA FIRST!", ...}
    tweets = [tweet1, tweet2, tweet3]
    to_text(all_caps_tweets(tweets))
    # => ["MAKE AMERICA SAFE AGAIN!", "AMERICA FIRST!"]
    '''

    return list(filter(lambda tweet: tweet['content'].isupper(), tweets))

def to_uppercase(tweets):
    return list(filter(lambda tweet: uppercase_helper(tweet), deepcopy(tweets)))

def uppercase_helper(tweet):
    return {**tweet, **{'content': tweet['content'].upper()}}

def count_individual_words(tweets):
    '''Counts all the words in all the tweets and returns the
    count as a dictionary mapping each word to its count.
    Example Uses:
    tweet1 = {"content": "MAKE AMERICA SAFE AGAIN!", ...}
    tweet2 = {"content": "america", ...}
    tweet3 = {"content": "AMERICA FIRST!", ...}
    tweets = [tweet1, tweet2, tweet3]
    count_individual_words(tweets)
    # => {
    # "MAKE": 1,
    # "AMERICA": 2,
    # "SAFE": 1,
    # "AGAIN!": 1,
    # "FIRST!": 1,
    # "america": 1,
    # }
    essentially : return dict(Counter(flatten((list(x+ ' ' for x in nonempty(tweets)))).split()))
    '''
    return dict(zip(words_as_list(tweets),
                    count_word(words_as_list(tweets))))

def count_word(tweets):
    return list(map(lambda word: reduce(lambda x, y: x + (y == word), tweets, 0), tweets))

def count_individual_hashtags(tweets):
    '''tweet1 = {"content": "#MAGA #Trump2016", ...}
    tweet2 = {"content": "#MakeAmericaGreatAgain", ...}
    tweet3 = {"content": "No hashtags in here.", ...}
    tweets = [tweet1, tweet2, tweet3]
    count_individual_hashtags(tweets)
    # => {
    # "#MAGA": 1,
    # "#Trump2016": 1,
    # "#MakeAmericaGreatAgain": 1,
    # }
    essentially: dict(Counter(all_hashtags(tweets)))
    '''
    return dict(zip(all_hashtags(tweets),
                    count_word(all_hashtags(tweets))))

def count_individual_mentions(tweets):
    '''Counts all the mentions in all the tweets and returns
    the count as a dictionary mapping each word to its count.
    Example Uses:
    tweet1 = {"content": "@cnn is fake news!", ...}
    tweet2 = {"content": "Can’t believe how many people buy @cnn fake news!", ...}
    tweet3 = {"content": "@marcorubio and I are friends now!", ...}
    tweets = [tweet1, tweet2, tweet3]
    count_individual_mentions(tweets)
    # => {
    # "@cnn": 2,
    # "@marcorubio": 1,
    # }
    essentially : return dict(Counter(all_mentions(tweets)))
    '''
    return dict(zip(all_mentions(tweets),
                    count_word(all_mentions(tweets))))

def n_most_common(n, word_count):
    '''Calculates the n most common keys in word_count ,
    sorted from most to least common and sorted in alphabetical order when the number of occurrences
    is the same.
    Example Uses:
    tweet1 = {"content": "MAKE AMERICA SAFE AGAIN!", ...}
    tweet2 = {"content": "america", ...}
    tweet3 = {"content": "AMERICA FIRST!", ...}
    tweets = [tweet1, tweet2, tweet3]
    n_most_common(1, count_individual_words(tweets)) # => [("AMERICA", 2)]
    '''
    return sorted(sorted(word_count.items(), key= itemgetter(0)), key = itemgetter(1), reverse= True)[:n]

def iphone_tweets(tweets):
    '''Filters a list of tweets to find only those made from an iPhone.
        Example Uses:
       tweet1 = {"content": "My hands are YUUGE!", "source": "Twitter for iPhone", ...}
        tweet2 = {"content": "#MakeAmericaOkAgain", "source": "Twitter for Android", ...}
        tweet3 = {"content": "#CrookedHillary", "source": "Twitter for iPhone", ...}
        tweets = [tweet1, tweet2, tweet3]
        to_text(iphone_tweets(tweets)) # => ["My hands are YUUGE!", "#CrookedHillary"]
        '''
    return list(filter(lambda tweet: tweet['source'] == 'Twitter for iPhone', tweets))

def android_tweets(tweets):
    '''Filters a list of tweets to find only those made from an Android
    device.
    Example Uses:
    tweet1 = {"content": "My hands are YUUGE!", "source": "Twitter for iPhone", ...}
    tweet2 = {"content": "#MakeAmericaOkAgain", "source": "Twitter for Android", ...}
    tweet3 = {"content": "I hate Little Marco.", "source": "Twitter for iPhone", ...}
    tweets = [tweet1, tweet2, tweet3]
    to_text(android_tweets(tweets)) # => ["#MakeAmericaOkAgain"]
    '''
    return list(filter(lambda tweet: tweet['source'] == 'Twitter for Android', tweets))

def average_favorites(tweets):
    '''– Computes the average number of favorites from the list of
    tweets, rounding appropriately.
    Example Uses:
    tweet1 = {"favorites": 32, ...}
    tweet2 = {"favorites": 8, ...}
    tweet3 = {"favorites": 16, ...}
    tweets = [tweet1, tweet2, tweet3]
    average_favorites(tweets) # => 19
    '''
    return round(reduce(lambda x, y: x + y,list(tweet['favorites'] for tweet in tweets))/len(tweets))

def average_retweets(tweets):
    '''Computes the average number of retweets from the list of
    tweets, rounding appropriately.
    Example Uses:
    tweet1 = {"retweets": 32, ...}
    tweet2 = {"retweets": 80, ...}
    tweet3 = {"retweets": 16, ...}
    tweets = [tweet1, tweet2, tweet3]
    average_retweets(tweets) # => 43
    '''
    return round(reduce(lambda x, y: x + y, list(tweet['retweets'] for tweet in tweets)) / len(tweets))

def sort_by_favorites(tweets):
    '''
    Sorts the tweets by the number of favorites they have.
    Example Uses:
    tweet1 = {"favorites": 32, ...}
    tweet2 = {"favorites": 8, ...}
    tweet3 = {"favorites": 16, ...}
    tweets = [tweet1, tweet2, tweet3]
    sort_by_favorites(tweets) # => [tweet2, tweet3, tweet1]
    '''
    return sorted(tweets, key= lambda tweet: tweet['favorites'])

def sort_by_retweets(tweets):
    '''
    Sorts the tweets by the number of favorites they have.
    Example Uses:
    tweet1 = {"favorites": 32, ...}
    tweet2 = {"favorites": 8, ...}
    tweet3 = {"favorites": 16, ...}
    tweets = [tweet1, tweet2, tweet3]
    sort_by_favorites(tweets) # => [tweet2, tweet3, tweet1]
    '''
    return sorted(tweets, key= lambda tweet: tweet['retweets'])

def upper_quartile(tweets):
    ''' Assuming the input is sorted, find the tweet representative of
    the upper quartile. This is the tweet representing the 75th percentile in the characteristic the list
    has been sorted by. You can compute it as 3/4th of the size of the input.
    Example Uses:
    tweet1 = {"favorites": 32, ...}
    tweet2 = {"favorites": 8, ...}
    tweet3 = {"favorites": 16, ...}
    tweet4 = {"favorites": 19, ...}
    tweet5 = {"favorites": 44, ...}
    tweets = [tweet1, tweet2, tweet3, tweet4, tweet5]
    upper_quartile(sort_by_favorites(tweets)) # => tweet1
    '''
    return tweets[int(.75 * (len(tweets) - 1))]

def lower_quartile(tweets):
    '''
    Assuming the input is sorted, find the tweet representative of
    the lower quartile. This is the tweet representing the 25th percentile in the characteristic the list
    has been sorted by. You can compute it as 1/4th of the size of the input.
    Example Uses:
    tweet1 = {"retweets": 32, ...}
    tweet2 = {"retweets": 8, ...}
    tweet3 = {"retweets": 16, ...}
    tweet4 = {"retweets": 19, ...}
    tweet5 = {"retweets": 44, ...}
    tweets = [tweet1, tweet2, tweet3, tweet4, tweet5]
    lower_quartile(sort_by_retweets(tweets)) # => tweet3
    '''
    return tweets[int(.25 * (len(tweets) - 1))]

def top_quarter_by(tweets, factor):
    '''Assuming the input is sorted by factor , find all
    tweets with factor greater than or equal to the upper quartile representative found using the
    upper_quartile function you’ve implemented.
    Example Uses:
    tweet1 = {"retweets": 32, ...}
    tweet2 = {"retweets": 8, ...}
    tweet3 = {"retweets": 16, ...}
    tweet4 = {"retweets": 19, ...}
    tweet5 = {"retweets": 44, ...}
    tweets = [tweet1, tweet2, tweet3, tweet4, tweet5]
    top_quarter_by(sort_by_retweets(tweets), "retweets") # => [tweet1, tweet5]
    '''
    return tweets[int(.75 * (len(tweets) - 1)):]

def bottom_quarter_by(tweets, factor):
    '''Assuming the input is sorted by factor , find
    all tweets with factor less than or equal to the lower quartile representative found using the
    lower_quartile function you’ve implemented.
    Example Uses:
    tweet1 = {"favorites": 32, ...}
    tweet2 = {"favorites": 8, ...}
    tweet3 = {"favorites": 16, ...}
    tweet4 = {"favorites": 19, ...}
    tweet5 = {"favorites": 44, ...}
    tweets = [tweet1, tweet2, tweet3, tweet4, tweet5]   8   16   19   32   44
    bottom_quarter_by(sort_by_favorites(tweets), "favorites") # => [tweet2, tweet3]
    '''
    return tweets[:int(.25 * (len(tweets) - 1)) + 1]