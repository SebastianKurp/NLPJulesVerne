#imports
from nltk import word_tokenize, pos_tag, ne_chunk
from nltk.chunk import conlltags2tree, tree2conlltags, ne_chunk
from nltk.tree import Tree

# #load data
processedText= 'Text-Cleaner(Update_3)/processed.txt'
file = open(processedText, encoding='utf-8')
text = file.read()
file.close()

#spilt the list into tokens
tokens = word_tokenize(text)

#POSTag the words
PosTag = pos_tag(tokens)

Print To Txt The Words And Tags, could probably do as a csv...
print(PosTag[:2])
POSTagged = open('POS(Update_4)/POSTagged.txt','w',encoding= 'utf-8')
for item in PosTag:
    POSTagged.write(str(item) + '\n' )
POSTagged.close()
print('POSTagged Exported')

#ShallowingParsing Portion(Chunking)
unprocessedText ='Text-Cleaner(Update_3)/2488.txt'
file2 = open(unprocessedText,encoding='utf-8')
sentText = file2.read()
file2.close()

sentTokens = sent_tokenize(sentText)

for item in sentTokens:
    sentTokens = word_tokenize(item)
    sentPosTag = pos_tag(sentTokens)
    
    nameEnt = ne_chunk(sentPosTag)
    #visualize the chunk trees.
    # nameEnt.draw()
#print to file chunk tree... takes a while.
chunkTree = open('POS(Update_4)/ChunkTree.txt')
chunkTree.writelines(nameEnt)
chunkTree.close()
print('ChunkText Exported')