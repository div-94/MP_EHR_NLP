import io
import os
from nltk.tokenize import RegexpTokenizer
from nltk.stem import WordNetLemmatizer
from nltk import pos_tag
from nltk.tokenize import PunktSentenceTokenizer

# check context of the token
# left two words and right two words
# ignore numbers
count = 0
dirpath = "C:\\Users\\Divya\\Desktop\\search"


def ans(word):
    for ind,x in enumerate(spl):
       if x.strip(",'.!")==word or x.strip(',".!')==word:
           break
    print(" ".join(spl[ind-2:ind]+spl[ind:ind+3]))

for filename in os.listdir(dirpath):
    print("ENTERINGG" + filename)
    while(count < 10):
        with open("C:\\Users\\Divya\\Desktop\\search\\" + filename) as f:
            lines = [line for line in f.readlines()]
            print("OKK")
        for line in lines:
            #tokenizer = RegexpTokenizer(r'\w+')
            #tokens = tokenizer.tokenize(line)
            #tokens_pos = pos_tag(tokens)
            spl = line.split()
            ans('sickle')
            #print(tokens_pos)
    count = count +1


'''def ans(word):
    for ind,x in enumerate(spl):
       if x.strip(",'.!")==word or x.strip(',".!')==word:
           break
    print(" ".join(spl[ind-2:ind]+spl[ind:ind+3]))

ans('abdomen')'''
