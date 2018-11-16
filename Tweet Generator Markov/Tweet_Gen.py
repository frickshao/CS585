from tweet_generator import tweet_generator
TPCK = 'zY3ajT3V3tdFVprsuCkLAVaTM'
TSCK = 'ziegcyepuWZGkqn6n87aXkdFCgETTwLLpRebdQ45abjc6Jp7AV'
TPAK = '198664917-vfTh0G91CS54EQIHWKj5jZLEOb2RcME1w31gwlit'
TSAK = '3fe6TNF80wMX3Uu49chcV4Ei9xhnQMwh2MohTV8q3etab'
twitter_bot = tweet_generator.PersonTweeter('iheartmindy',TPCK,TSCK,TPAK,TSAK)
for i in range(100):
    random_tweet = twitter_bot.generate_random_tweet()
    print(random_tweet)
    print()
