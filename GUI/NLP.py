from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import nltk
import re

def break_into_token(text):
    # resource required to run the program
    # nltk.download('punkt') # uncomment to download

    #Cleaning
    text = re.sub("<[^>]+>", "", text).strip()
    text = text.replace("\n", " ")

    #Tokenization
    word = word_tokenize(text)

    #Lowercase
    for i in range(0, len(word)):
        word[i] = word[i].lower()

    #Remove delimiter
    i = 0
    length = len(word)
    while True:
        if i == length:
            break
        #if(bool(re.search('^[a-zA-Z0-9]*$', word[i]))==False): #Remove word with number too
        if(bool(re.search('^[a-zA-Z]*$', word[i]))==False):
            del word[i]
            length-=1
        else:
            i+=1
            
    return word

def stop_list(word):
    #Stoplist (Stopword Removal)
    #nltk.download('stopwords') #Uncomment to download package
    english_stops = set(stopwords.words('english'))
    i = 0
    length = len(word)
    while True:
        if i == length:
            break
        if(word[i] in english_stops):
            del word[i]
            length-=1
        else:
            i+=1
    
    return word

def stemming(word):
    #Porter Stemming
    # for i in range(0, len(word)):
    #     word[i] = PorterStemmer().stem(word[i])

    w = []
    for i in word:
        w.append(PorterStemmer().stem(i))
    
    return w