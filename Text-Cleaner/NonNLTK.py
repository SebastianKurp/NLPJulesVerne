import re
import string

#load text(s)
filename ='pg2488.txt'
file = open(filename, encoding="utf8" )
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
