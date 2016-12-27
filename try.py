import io
import os
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
mainpath="C:\\Users\\Divya\\Desktop\\FILES\\HIGHLY SPECIFIED"

#OUTER MOST FOR LOOP
for filenamemain in os.listdir(mainpath):
    file_object = open(mainpath + "\\" + filenamemain)
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

    new_list = [x for x in tokens if not (x.isdigit() or x[0] == '-' and x[1:].isdigit())]
#print(no_integers)

#stopword removal
    english_stops = set(stopwords.words('english'))
    words = new_list
    lemma = WordNetLemmatizer()

    myList = [lemma.lemmatize(word,pos='v') for word in words if word not in english_stops]
    print (myList)

#POS tagging
    tokens_pos = pos_tag(myList)
    print(tokens_pos)

#dt_tags = [t for t in tokens_pos if t[1] == "NNP"]
#print(dt_tags)

#postagged tokens are saved to file
    '''
    f = open("C:\\Users\\Divya\\Desktop\\jump5.txt", "w")
        for i in tokens_pos:
        f.write(str(i)+'\n')
    '''
    #search for reult of token from SNOMEDCT ontology
    fnamev, file_extension = os.path.splitext(filenamemain)
    mp="C:\\Users\\Divya\\SOME\\"+ fnamev
    print(mp)

    def make_sure_path_exists(path):
            os.makedirs(path,exist_ok=True)


    make_sure_path_exists(mp)
    for i in myList:
        jj = SNOMEDCT.search(i) #the  datatype of jj is snomedct type
        with io.open(mp + "\\" + str(i) + ".txt", 'w', encoding='utf-8') as f: #save the results in file
            f.write(str(jj)+'\n')
    print("donee")
    #new code to remove empty files

    for fnameff in os.listdir(mp):
        with open(mp + "\\" + fnameff) as f:
            lines = f.readlines()
            if str(lines) == "[]":
                print(fnameff)
                os.remove(fnameff)

    print("ok")