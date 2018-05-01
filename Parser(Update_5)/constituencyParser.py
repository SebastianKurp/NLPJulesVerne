#imports
from nltk import RecursiveDescentParser, ShiftReduceParser, sent_tokenize
from nltk.tree import Tree
from nltk.grammar import PCFG

import random

#Load Data
unprocessedText ='Text-Cleaner(Update_3)/2488.txt'
file = open(unprocessedText,encoding='utf-8')
sentText = file.read()
file.close()

#Grammar Rules
grammar = nltk.parse_cfg("""
S -> NP VP
NP -> 'DT' 'NN'
VP -> 'VB'
VP -> 'VB' 'NN'
"""
#Tokenize's the data into sentences
sentTokens = sent_tokenize(sentText)

#Recursive Descent Parsing
rd_parser = RecursiveDescentParser(PCFG)
for tree in rd_parser.parse(sentTokens):
    print(tree)
    
# #Shift Reduce Parser
# sr_parser = ShiftReduceParser(PCFG)
# for tree in sr_parser.parse(oneSent):
#     print(tree)
