from textblob import TextBlob
import csv
from preprocess import clean_tweet
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def sentiment_analysis(tweet):
    def getSubjectivity(text):
        return TextBlob(text).sentiment.subjectivity

    #Create a function to get the polarity
    def getPolarity(text):
        return TextBlob(text).sentiment.polarity

    #Create two new columns ‘Subjectivity' & ‘Polarity'
    result= {}
    result['TextBlob_Subjectivity'] = getSubjectivity(tweet)
    result ['TextBlob_Polarity'] = getPolarity(tweet)
    def getAnalysis(score):
        if score < 0:
            return 'Negative'
        elif score == 0:
            return 'Neutral'
        else:
            return 'Positive'
    result ['Sentiment'] = getAnalysis(result ['TextBlob_Polarity'])
    return result


#read csv file
with open('tweets_ronaldo_50.csv', mode="r") as csv_file: #"r" represents the read mode
    reader = csv.reader(csv_file) #this is the reader object
    tweets =[]
    for item in reader:
        tweets.append(item[1])

#preprocess text to remove stop words, punctuation, links and so on

# print(tweets[:6])
results = [clean_tweet(tw) for tw in tweets]

# text = TextBlob(results[2])
# print(text.sentiment)
# quit();

tweet_text = results[25]
result = sentiment_analysis(tweet_text)
print(tweet_text)
print(result)



sentiment =  SentimentIntensityAnalyzer()
# text_1 = results[25]
# sent_1 =  sentiment.polarity_scores(text_1)
# print("Sentiment of text 1:", sent_1)

def get_maximum_key(d):
  return max(d, key = d.get)

# read the csv file containing tweets and get sentiment of each row and add its value to new column

sentiments_labels = {'neg': 'NEGATIVE','neu':'NEUTRAL','pos':'POSITIVE','compound':'COMPOUND'}

with open('tweets_ronaldo_50.csv','r') as csvinput:
    with open('output.csv', 'w') as csvoutput:
        writer = csv.writer(csvoutput, lineterminator='\n')
        reader = csv.reader(csvinput)

        all = []
        row = next(reader)
        
        row.append('Sentiment')
        row.append('Stance')
        all.append(row)

        for row in reader:
            # print("The tweet for sentiment",row[1])
            row[1] = clean_tweet(row[1])
            sentiment_polarity = sentiment.polarity_scores(row[0])
            print("Tweet is ::: ", row[1])
            stance = input("Enter your stance: Ronaldo is better than messi ")
            sentiment_value = get_maximum_key(sentiment_polarity)
            row.append(sentiments_labels[sentiment_value])
            row.append(stance)
            all.append(row)

        writer.writerows(all)





#issue
# You fucking bow to Ronaldo you absolute melt , sentiment analysis will give negative polarity
# 1 ronaldo 2 maradona 3 pele 4 messi thats what i think and feel, sentiment analysis will give neutral polarity 15,2,6,25