#Simple non-NLTK Lib, only splits the words,removes whitespace and makes every word lowercase
#TODO: Add a stop word remover, reorder the the task for improvement on speed.
import re
import string
#load text(s)
filename = '2488.txt'
file = open(filename, encoding='utf8' )
text = file.read()
file.close()
#split text by whitespace
words = text.split()
#remove punctuation from each word
table = str.maketrans('', '', string.punctuation)
stripped = [w.translate(table) for w in words ]
#Make everything lowercase
clean = [stripped.lower() for word in stripped]

#print for testing
print(stripped[:20])
