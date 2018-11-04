import tweepy
import json
import configparser
import os
import html
import sys
import time
import re


emoji_pattern = re.compile("["
     #   u"\U0001F600-\U0001F64F"  # emoticons
     #   u"\U0001F300-\U0001F5FF"  # symbols & pictographs
     #   u"\U0001F680-\U0001F6FF"  # transport & map symbols
     #   u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
        u"\U0001F600-\U0010ffff"
                           "]+", flags=re.UNICODE)

# Read in twitter.ini as a configuration to get API keys.
parser = configparser.ConfigParser()
parser.read("config.ini")
twitter = parser["Twitter"]




# authorize twitter, initialize tweepy
auth = tweepy.OAuthHandler(twitter["consumer_key"], twitter["consumer_secret"])
auth.set_access_token(twitter["access_token_key"],twitter["access_token_secret"])
api = tweepy.API(auth)
print("> Twitter API access success!")

#Twitter User screenname
try:
	if sys.argv[0] == "tweet_downloader.py" or sys.argv[0] == "C:/Users/quanb/PycharmProjects/tweet_scrapper/tweet_downloader.py":
		screen_name = sys.argv[1]
	else:
		screen_name = sys.argv[0]
except:
	screen_name = twitter["screen_name"]

if len(screen_name) == 0:
	screen_name = twitter["screen_name"]
	
print("> downloading tweets from ", screen_name)
	
# list of user tweets
user_tweets = []

# request for tweets, save them, save the id of the oldest one (max_id)
try:
	recent_tweets = api.user_timeline(screen_name=screen_name,
									  count=200,
									  include_rts=False,
									  exclude_replies=False,
									  tweet_mode = "extended")
except Exception:
	print("> ERROR: Not a valid screen name!")
	quit()
user_tweets.extend(recent_tweets)
max_id = user_tweets[-1].id - 1

while len(recent_tweets) > 0:
    recent_tweets = api.user_timeline(screen_name=screen_name,
                                      count=200,
                                      include_rts=False,
                                      exclude_replies=False,
                                      max_id=max_id,
                                      tweet_mode = "extended")

    # save most recent tweets
    user_tweets.extend(recent_tweets)
    max_id = user_tweets[-1].id - 1

    print("> {0:4} tweets saved!".format(len(user_tweets)))

print("> Finished with ", len(user_tweets), " tweets saved!")

# Grabs the tweet objects we want.
def format_tweet(tweet):
    return {
        "tweet_id" : tweet.id,
        "username": tweet.user.name,
        "mentions" : tweet.entities["user_mentions"],
        "text": tweet.full_text,
        "text_no_emoji": emoji_pattern.sub(r'', tweet.full_text),
        "hashtags" : tweet.entities["hashtags"],
        "links": tweet.entities["urls"],
        "favorites": tweet.favorite_count,
        "retweets": tweet.retweet_count,
        "source" : tweet.source
    }
formatted_tweets = list(map(format_tweet, user_tweets))

try:
    # Creates tweets folder
    os.mkdir("tweets")
except:
    pass

save_path = "tweets/@" + screen_name + "/"

try:
    # Creates user folders
    os.mkdir(save_path)
    print("> Directory " , save_path ,  " Created ")
except FileExistsError:
    print("> Directory " , save_path ,  " already exists")

# Write to json
file_name = "tweets.json"
completeName = os.path.join(save_path, file_name)
with open(completeName, "w") as output:
    json.dump(formatted_tweets, output)
print("> Created ", file_name, " in ", save_path)


def get_info(screen_name):
    user = api.get_user(screen_name)
    return {
        "screen_name" : user.screen_name,
        "description" : user.description,
        "followers" : user.followers_count,
        "statuses_count" : user.statuses_count,
        "url" : user.url,
		"date_accessed" : time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    }

#creates a user info file
file_name = "info.json"
completeName = os.path.join(save_path, file_name)
with open(completeName, "w") as output:
    json.dump(get_info(screen_name), output)
print("> Created ", file_name, " in ", save_path)

#creates a file of full info
def pull_status_obj(tweet):
    return {
        "json" : tweet._json
    }
status_json = list(map(pull_status_obj, user_tweets))

file_name = 'full_tweets.json'
completeName = os.path.join(save_path, file_name)
with open(completeName, "w") as output:
    json.dump(status_json, output)
print("> Created ", file_name, " in ", save_path)