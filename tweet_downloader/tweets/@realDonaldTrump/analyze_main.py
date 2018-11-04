from analyze import *

#text_file = open("Output.txt", "w")
'''
print(to_text(tweets[:100]))
print(to_lowercase(tweets[:100]))
print(nonempty(tweets[:100]))
print(total_word_count(tweets[:100]))
print(all_hashtags(tweets[:100]))
print(all_mentions(tweets[:100]))
print(all_caps_tweets(tweets[:100]))
print(count_individual_words(tweets[:100]))
print(count_individual_hashtags(tweets[:100]))
print(count_individual_mentions(tweets[:100]))
print(n_most_common(5, count_individual_words(tweets[:100])))
print(iphone_tweets(tweets[:100]))
print(android_tweets(tweets[:100]))
print(average_favorites(tweets[:100]))
print(average_retweets(tweets[:100]))
print(to_text(sort_by_favorites(tweets[:100])))
print(to_text(sort_by_retweets(tweets[:100])))
print(upper_quartile(tweets[:100]))
print(lower_quartile(tweets[:100]))
print(top_quarter_by(tweets[:100], None))
print(bottom_quarter_by(tweets[:100], None))'''

print("Total Words: ", total_word_count(tweets))
print("Total Hashtags:", len(all_hashtags(tweets)))
print("Total Mentions: ", len(all_mentions(tweets)))

print("Hashtags: ", all_hashtags(tweets))
print("Mentions: ", all_mentions(tweets))


print("Using 100 most recent tweets")
print("Total Individual Words: ", count_individual_words(tweets[:100]))
print("Total Individual Hashtags: ", count_individual_hashtags(tweets[:100]))
print("Total Individual Mentions: ", count_individual_mentions(tweets[:100]))

print("20 most common words: ", n_most_common(20, count_individual_words(tweets[:100])))