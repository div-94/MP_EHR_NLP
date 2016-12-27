from nltk import ngrams
import io
import errno
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk import pos_tag
from nltk.tokenize import PunktSentenceTokenizer
import pymedtermino
pymedtermino.LANGUAGE = "en"
pymedtermino.REMOVE_SUPPRESSED_CONCEPTS = True
from pymedtermino import *
from pymedtermino.snomedct import *


#read tokens
file_object = open("C:\\Users\\Divya\\Desktop\\jumlist.txt")
para = file_object.read()
#split into tokens
listtok = para.split()

n1=2
n2=3
bigrms = ngrams(para.split(),n1) #create bigrams
trigrms = ngrams(para.split(),n2) #create trigrams
listbi = []
listtri = []
for grms1 in bigrms:
    listbi.append(grms1)
for grms2 in trigrms:
    listtri.append(grms2)

#print(listtok)
#print(listbi)
#print(listtri)
tokens_pos = pos_tag(listtok)
print(tokens_pos)

print(listbi)
for item in listbi:
    listbit = ' '.join(item)
    print(listbit)
    tokbi_pos = pos_tag(listbit)
    print("kk")
'''
for item in listbi:
    listbit = ''.join(item)
    tokbi_pos = pos_tag(listbit)
    print(tokbi_pos)

toktri_pos = pos_tag(listtri)
print(toktri_pos)

for i in listtok:
    jj = SNOMEDCT.search(i)  # the  datatype of jj is snomedct type
    if jj == []:
        # print('NONE')
        continue
    else:
        print("SNOMEDCT gives result")
        if



with io.open(mp + "\\" + str(i) + ".txt", 'w', encoding='utf-8') as f:  # save the results in file
    f.write(str(jj) + '\n')

'''