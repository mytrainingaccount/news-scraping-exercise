#MEASURING SENTIMENT ABOUT CHINA FROM REUTERS NEWS WIRE

#This code will pull out all sentences from the "text"
#portion of the Reuters Wire data that mention "China."
#It will then utilize Textblob's sentiment analysis 
#feature to provide an approximation of the sentiment of
#the sentences that mention China.
#To do this, it will utilize Pickle 4.0, Textblob 15.4, 
#numpy 1.18.1, and Python 3.7.6.

#SETUP THE DATA
#(below was thanks to assistance from Dr. Pike)
#First we will load the saved Reuters pickle file
import pickle
news_article = pickle.load(open('/Users/me/news-scraping-exercise/news_dump_object.pkl','rb'))

#The data in the pickle file is actually a list of dictionaries
#and the wordcloud library takes input as a long string.  
#The below creates an empty string called "cloud_text" where
#we will add all the text portions from the pickle file.
cloud_text = ''

#The below code iterates through the loaded pickle file and adds
#each value associated wih the key to the empty strings made earlier.
for article in news_article:
     cloud_text+=article['Text']+' '


#SENTIMENT ANALYSIS
#After importing Textblob, we set it up to run on the previously
#defined cloud_text and to compartmentalize the text into sentences.
from textblob import TextBlob

blob = TextBlob(cloud_text)
blob_sentences = blob.sentences

#We set up an empty list called "filtered_sentences" and iterate through
#each of the sentences that textblob compartmentalized (blob_sentences).
#Whenever a sentence containing "China" is found, the sentence will be
#appended to the empty list filtered_sentences.
filtered_sentences = [] 

for sentence in blob_sentences: 
    if 'China' in sentence: filtered_sentences.append(sentence)
    
#print(filtered_sentences)
#print(filtered_sentences[1].sentiment)

#We create an empty list "China_sentiment" and iterate through the 
#filtered_sentences, having Textblob apply a "polarity" and "subjectivity"
#value to each sentence, multiply them by each other to get a "sentiment"
#value, then append those scores to the empty list.
China_sentiment = [] 

for sentence in filtered_sentences: 
    sentiment = sentence.sentiment[0]*sentence.sentiment[1] 
    China_sentiment.append(sentiment)

#print(China_sentiment)

#Using Numpy, we find an average of all of the sentences' sentiment scores
#to come to an average sentiment value for all sentences mentioning China.
import numpy as np 

China_avg_sentiment = np.average(China_sentiment)

print(China_avg_sentiment)