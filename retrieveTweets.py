import csv
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
    return list(x['text_no_emoji'].lower() for x in tweets)

#creating a list of lowercase tweets
lst = to_text(tweets)
#print(lst)

#exporting this list to a csv
out = open('tweets.csv', 'w+', encoding = 'utf-8')
writer = csv.writer(out, quoting = csv.QUOTE_ALL)
writer.writerow(lst)
out.close()

"""
how to import the csv to a list, for whatever reason it produces a list of lists were the first sublist is all the tweets
the second sublist is empty so my_list[0] is our list of tweets
with open('tweets.csv', 'r', encoding = 'utf-8') as f:
    reader = csv.reader(f)
    my_list = list(reader)
print(my_list[0])
"""

#converting our lst to a string, where each paragraph is a single tweet
string = ''
for x in lst:
    string = string + x + '\n' + '\n'
#print(string)

#exporting the string to a text file
text_file = open('tweets.txt', 'w+', encoding = 'utf-8')
text_file.write(string)
text_file.close()

"""
how to import the text to a string
string = open('tweets.txt', 'r', encoding = 'utf-8').read()
#print(string)
"""























