#CREATING WORD CLOUDS FROM REUTERS NEWS WIRE

#This code will generate two word clouds from the text and the titles
#of the news scraped from the reuters website and saved as a pickle file.  
#To do this, it will utilize Wordcloud version 1.7.0 and matplotlib 3.2.1,
#Pickle 4.0, and Python 3.7.6.


#SETUP THE DATA
#(below was thanks to assistance from Dr. Pike)
#First we will load the saved Reuters pickle file
import pickle
news_article = pickle.load(open('/Users/me/news-scraping-exercise/news_dump_object.pkl','rb'))

#The data in the pickle file is actually a list of dictionaries
#and the wordcloud library takes input as a long string.  
#The below creates two empty strings called "cloud_title" where
#we will add all the titles from the pickle file, and "cloud_text"
#where we will add the text portions. 
cloud_title = ''
cloud_text = ''

#The below code iterates through the loaded pickle file and adds
#each value associated wih the key to the empty strings made earlier.
for article in news_article:
    cloud_title+=article['Title']+' '
    cloud_text+=article['Text']+' '
#   print(article.keys())
#   break


#MAKING A WORDCLOUD
#We will import wordcloud to generate the cloud, and matplotlib
#to display the results.  This should generate two wordclouds,
#one based on mentions in the article text and one based on
#mentions in the article titles.  We also will import the
#WordCloud STOPWORDS set of common words like "the, a" etc,
#and will set the Wordcloud attribute "stopwords" to exclude that
#set of words, with a few others that were not in the list.
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

cutwords = set(STOPWORDS)
cutwords.add("said")
cutwords.add("say")

newstext_wordcloud = WordCloud(max_font_size=40, stopwords=cutwords).generate(cloud_text)
plt.imshow(newstext_wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()

newstitle_wordcloud = WordCloud(max_font_size=40, stopwords=cutwords).generate(cloud_title)
plt.imshow(newstitle_wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()
