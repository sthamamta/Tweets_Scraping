#this program reads csv file containing tweets and preprocess it and generate wordcloud
from preprocess import clean_tweet
import csv 
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from collections import Counter
from nltk.corpus import stopwords


#read csv file
with open('tweets_csv/tweets_mbappe_50000.csv', mode="r") as csv_file: #"r" represents the read mode
    reader = csv.reader(csv_file) #this is the reader object
    tweets =[]
    for item in reader:
        tweets.append(item[1])

#preprocess text to remove stop words, punctuation, links and so on

print(tweets[:10])
results = [clean_tweet(tw) for tw in tweets] #get list of preprocessed tweets
results = [word for line in results for word in line.split()]  #get list of words
print("***********************************************************************************************************************************************************************")
print(results[:10])

word_could_dict = Counter(results)
print("***********************************************************************************************************************************************************************")
remove_keys = [ 'is','the','are', 'i','you','that','of','and','has','to','a','was','with','in','he','his','for','this','we','there','if','him','us']
remove_keys = []
for key in remove_keys:
    del word_could_dict[key]

# wordcloud = WordCloud(width = 1000, height = 500).generate_from_frequencies(word_could_dict)
file_content=open ("tweets_csv/tweets_mbappe_50000.csv").read()
wordcloud = WordCloud(stopwords = remove_keys,
                            # background_color = 'white',
                            width = 1200,
                            height = 1000,
                            collocation_threshold = 2              
                            ).generate(file_content)

plt.figure(figsize=(15,8))
plt.imshow(wordcloud, interpolation='bilInear')
plt.axis("off")
#plt.show()
plt.savefig('mbappe_wordcloud_50000.png', bbox_inches='tight')
plt.close()


# wordcloud = WordCloud(stopwords = stopwords,
#                       collocations=True).generate(results)



# text_dictionary = wordcloud.process_text(results)
# # sort the dictionary
# word_freq={k: v for k, v in sorted(text_dictionary.items(),reverse=True, key=lambda item: item[1])}

# #use words_ to print relative word frequencies
# rel_freq=wordcloud.words_

# #print results
# print(list(word_freq.items())[:5])
# print(list(rel_freq.items())[:5])

# wordcloud = WordCloud(font_path = r'C:\Windows\Fonts\Verdana.ttf',
#                             stopwords = STOPWORDS,
#                             background_color = 'white',
#                             width = 1200,
#                             height = 1000,
#                             color_func = random_color_func,
#                             collocation_threshold = 3               --added this to your question code, try changing this value between 1-50
#                             ).generate(file_content)