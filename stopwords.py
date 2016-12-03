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
#MAIN FOLDER PATH
mainpath= "C:\\Users\\Divya\\Desktop\\"
lonne = "senttok"

#OUTER MOST FOR LOOP
#for filenamemain in os.listdir(mainpath):
#file_object = open(mainpath+ "\\" +filenamemain)
file_object = open(mainpath + "ehr.txt")
para = file_object.read()

'''#sentence boundary
    sent_tokenize = PunktSentenceTokenizer()
    sent_tokenize_list = sent_tokenize.tokenize(para)
    #print(len(sent_tokenize_list))
    #print(sent_tokenize_list)
    f = open("C:\\Users\\Divya\\Desktop\\sentd5.txt", "w")
    for i in sent_tokenize_list:
    f.write(str(i)+'\t')
'''
#tokenize
tokenizer = RegexpTokenizer(r'\w+')
#tokenizer = TreebankWordTokenizer()
tokens = tokenizer.tokenize(para)
print(tokens)

new_list = [x for x in tokens if not (x.isdigit()
                                         or x[0] == '-' and x[1:].isdigit())]
#print(no_integers)

#stopword removal
english_stops = set(stopwords.words('english'))
print(english_stops)
count1 = 0
count2 = 0
count3 = 0
words = new_list
myList = []
lemma = WordNetLemmatizer()
for word in words:
    if word not in english_stops:
        lemma.lemmatize(word,pos='v')
        count1 = count1 + 1
        myList.append(word)


dict = ['in','address','the','of','ï','ÂµL','â','_____________________']
for word in myList:
    if word not in dict:
        count2 = count2 + 1
        myList.append(word)

print(count1)
print(count2)



#POS tagging
tokens_pos = pos_tag(myList)
print(tokens_pos)
