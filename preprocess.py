import numpy as np
import re
from nltk.corpus import stopwords
from tqdm import tqdm
import nltk
nltk.download('punkt')
import matplotlib.pyplot as plt
from wordcloud import WordCloud

contractions = { "ain't": "am not / are not", "aren't": "are not / am not", "can't": "cannot", "can't've": "cannot have", "'cause": "because", "could've": "could have",
 "couldn't": "could not", "couldn't've": "could not have", "didn't": "did not", "doesn't": "does not", "don\'t": "do not", "hadn\'t": "had not", "hadn't've": "had not have",
  "hasn't": "has not", "haven't": "have not", "he'd": "he had / he would", "he'd've": "he would have", "he'll": "he shall / he will", "he'll've": "he shall have / he will have", 
  "he's": "he has / he is", "how'd": "how did", "how'd'y": "how do you", "how'll": "how will", "how's": "how has / how is", "i'd": "I had / I would", "i'd've": "I would have", 
  "i'll": "I shall / I will", "i'll've": "I shall have / I will have", "i'm": "I am", "i've": "I have", "isn't": "is not", "it'd": "it had / it would", "it'd've": "it would have"
  , "it'll": "it shall / it will", "it'll've": "it shall have / it will have", "it's": "it has / it is", "let's": "let us", "ma'am": "madam", "mayn't": "may not", "might've": 
  "might have", "mightn't": "might not", "mightn't've": "might not have", "must've": "must have", "mustn't": "must not", "mustn't've": "must not have", "needn't": "need not", 
  "needn't've": "need not have", "o'clock": "of the clock", "oughtn't": "ought not", "oughtn't've": "ought not have", "shan't": "shall not", "sha'n't": "shall not", "shan't've":
   "shall not have", "she'd": "she had / she would", "she'd've": "she would have", "she'll": "she shall / she will", "she'll've": "she shall have / she will have", "she's": "she has / she is", "should've": "should have", "shouldn\'t": "should not", "shouldn\'t\'ve": "should not have", "so\'ve": "so have", "so\'s": "so as / so is", "that\'d": "that would / that had", "that\'d\'ve": "that would have", "that's": "that has / that is", "there'd": "there had / there would", "there'd've": "there would have", "there's": "there has / there is", "they'd": "they had / they would", "they'd've": "they would have", "they'll": "they shall / they will", "they'll've": "they shall have / they will have", 
    "they're": "they are", "they've": "they have", "to've": "to have", "wasn't": "was not", "we'd": "we had / we would", "we'd've": "we would have", "we'll": "we will", 
    "we'll've": "we will have", "we're": "we are", "we've": "we have", "weren't": "were not", "what'll": "what shall / what will", "what'll've": "what shall have / what will have", "what're": "what are", "what's": "what has / what is", "what've": "what have", "when's": "when has / when is", "when've": "when have", "where'd": "where did", "where's": "where has / where is", "where've": "where have", "who'll": "who shall / who will", "who'll've": "who shall have / who will have", "who's": "who has / who is", "who've": "who have", "why's": "why has / why is", "why've": "why have", "will've": "will have", "won't": "will not", "won't've": "will not have", "would've": "would have", "wouldn't": "would not", "wouldn't've": "would not have", "y'all": "you all", "y'all'd": "you all would", "y'all'd've": "you all would have", "y'all're": "you all are", "y'all've": "you all have", "you'd": "you had / you would", "you'd've": "you would have", "you'll": "you shall / you will", "you'll've": "you shall have / you will have", "you're": "you are", "you've": "you have",
    "hadn\'t": "had not","wouldn\'t":"would not", "Don\'t":"Do not"
     }


def clean_tweet(tweet):
    if type(tweet) == np.float32:
        return ""
    temp = tweet.lower() #converting texts to lower case
    temp = re.sub("'", "", temp) # to avoid removing contractions in english
    temp = re.sub("@[A-Za-z0-9_]+","", temp) #removing mentions
    temp = re.sub("#[A-Za-z0-9_]+","", temp)  #removing hashtags
    temp = re.sub(r'http\S+', '', temp) #removing links
    temp = re.sub(r"www.\S+", "", temp) #removing links
    temp = re.sub('[()!?]', ' ', temp) #removing punctuation
    temp = re.sub('\[.*?\]',' ', temp) #removing punctuation
    temp = re.sub("[^a-z0-9]"," ", temp) #removing non-alpha numeric character
    for word in temp.split(): #remove the contractions in a text
        if word.lower() in contractions:
            temp = temp.replace(word,contractions[word.lower()])
            print("replace {} with {}".format(word, contractions[word.lower()]))
    temp = temp.split() #tokenize the sentence
    clean_text = []
    #removing stop words
    for word in temp:
        if word.lower() not in [stopwords]:
            clean_text.append(word)
    temp = " ".join(word for word in clean_text)
    return temp

if __name__ == "__main__":
    tweets = ["Get ready for #NatGeoEarthDay! Join us on 4/21 for an evening of music and celebration, exploration and inspiration https://on.natgeo.com/3t0wzQy.",
    "Coral in the shallows of Aitutaki Lagoon, Cook Islands, Polynesia https://on.natgeo.com/3gkgq4Z",
    "Don't miss our @reddit AMA with author and climber Mark Synnott who will be answering your questions about his historic journey to the North Face of Everest TODAY at 12:00pm ET! Start submitting your questions here: https://on.natgeo.com/3ddSkHk @DuttonBooks",
    "There is a mistake but I don't want to correct it."]

    results = [clean_tweet(tw) for tw in tweets]
    # print(results)

    from collections import Counter
    word_could_dict=Counter(results)
    wordcloud = WordCloud(width = 1000, height = 500).generate_from_frequencies(word_could_dict)

    plt.figure(figsize=(15,8))
    plt.imshow(wordcloud)
    plt.axis("off")
    #plt.show()
    plt.savefig('yourfile.png', bbox_inches='tight')
    plt.close()