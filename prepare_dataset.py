import csv
from preprocess import clean_tweet



with open('tweets_messi_25.csv','r') as csvinput:
    with open('ronaldo_test.csv', 'w') as csvoutput:
        writer = csv.writer(csvoutput, lineterminator='\n')

        reader = csv.reader(csvinput)

        all = []
        # all.append('Tweet')
        # all.append('Stance')
        # all.append('Index')
        # all.append('Original Tweet')
        index = 1
        for row in reader:
            new_row = []
            cleaned_tweet = clean_tweet(row[1])
            print("*********************************************************************************************************")
            print("Tweet is ::: ", row[1])
            stance = input("Enter your stance: Ronaldo is better than messi ")
            if stance == 'f':
                stance = 'FAVOR'
            elif stance == 'a':
                stance = 'AGAINST'
            else:
                stance = 'NONE'
            new_row.append(cleaned_tweet)
            new_row.append(stance)
            new_row.append(index)
            new_row.append(row[1])

            all.append(new_row)
            index +=1

        writer.writerows(all)





#issue
# You fucking bow to Ronaldo you absolute melt , sentiment analysis will give negative polarity
# 1 ronaldo 2 maradona 3 pele 4 messi thats what i think and feel, sentiment analysis will give neutral polarity 15,2,6,25