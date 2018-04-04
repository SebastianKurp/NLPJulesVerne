#Imports
import PyPDF2 
import textract
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

filename = 'enter the name of the file here' 

pdfFileObj = open(filename,'rb')

pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

num_pages = pdfReader.numPages
count = 0
text = ""

while count < num_pages:
    pageObj = pdfReader.getPage(count)
    count +=1
    text += pageObj.extractText()

if text != "":
   text = text
 
else:
   text = textract.process(fileurl, method='tesseract', language='eng')

tokens = word_tokenize(text)

punctuations = ['(',')',';',':','[',']',',']

stop_words = stopwords.words('english')
#Remove stop words and punctuation from the parse pdf
keywords = [word for word in tokens if not word in stop_words and  not word in string.punctuation]
#Make lowerCase from keywords
lowerKeyword =[stripped.lower() for word in keyword]

print(words[:100])
