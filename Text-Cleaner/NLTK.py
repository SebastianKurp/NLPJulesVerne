#imports
import string
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

#load data
filename = 'Text-Cleaner/2488.txt'
file = open(filename, encoding='utf-8' )
text = file.read()
file.close()

#split into words
tokens = word_tokenize(text)

# remove all tokens that are not alphabetic
nonAlphaWords = [word for word in tokens if word.isalpha()]

#filter out stop words
stop_words = set(stopwords.words('english'))
nonStopWords = [w for w in nonAlphaWords if not w in stop_words]

#stemming of words
porter = PorterStemmer()
stemmedWords = [porter.stem(word) for word in nonStopWords]

#prints the tokenized words to a text file
print(stemmedWords[:20])
processed = open('Text-Cleaner/processed.txt','w',encoding='utf-8')
for word in stemmedWords:
    processed.write('\n'+ word) 
processed.close()

print('Text Exported')