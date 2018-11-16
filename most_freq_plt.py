#for creating a histogram that depicts the 50 most common words in the supplied text file
from collections import Counter
import numpy as np
import matplotlib.pyplot as plt

words = open('tweets.txt', 'r').read()
words = words.split()
word_count = map(lambda w:(w, words.count(w)),set(words))
bow = dict(word_count)


bow_cnt = Counter(bow)
sorted_list = dict(bow_cnt.most_common(50))

#print(sorted_list)

labels = list(sorted_list.keys())
values = list(sorted_list.values())
#print(labels)
#print(values)

indexes = np.arange(len(labels))
width = 1
plt.bar(indexes, values, 1)
plt.xticks(indexes, labels, rotation = 'vertical')
plt.show()


