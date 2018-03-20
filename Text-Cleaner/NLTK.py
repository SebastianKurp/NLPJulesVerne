#TODO:Add array for texts
#imports
import string

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

#load data
filename = '2488.txt'
file = open(filename, 'rt')
text = file.read()
file.close()

#split into words
tokens = word_tokenize(text)

#convert to lower case
tokens = [w.lower() for w in tokens]

#remove punctuation from each word
table = str.maketrans('', '', string.punctuation)
stripped = [w.translate(table) for w in tokens]

#remove remaining tokens that are not alphabetic
words = [word for word in stripped if word.isalpha()]

#filter out stop words
stop_words = set(stopwords.words('english'))
words = [w for w in words if not w in stop_words]

#prints the first 100 words as a test... switch 
print(words[:100])