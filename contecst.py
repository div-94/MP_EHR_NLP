import io
import errno
import os
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
# tokenize
tokenizer = RegexpTokenizer(r'\w+')
# tokenizer = TreebankWordTokenizer()
tokens = tokenizer.tokenize(para)
#print(tokens)
#with io.open(mainpath + "\\" + lonne + ".txt", 'w', encoding='utf-8') as f:  # save the results in file
 #   f.write(str(tokens))
new_list = [x for x in tokens if not (x.isdigit() or x[0] == '-' and x[1:].isdigit())]
#with io.open(mainpath + "\\" + lonne + ".txt", 'w', encoding='utf-8') as f:  # save the results in file
 #   for item in new_list:
  #      f.write("{}\n".format(item))

# print(no_integers)
# stopword removal
english_stops = set(stopwords.words('english'))
print(english_stops)
words = new_list
lemma = WordNetLemmatizer()
myList = [lemma.lemmatize(word, pos='v') for word in words if word not in english_stops]
#print(myList)

exit = ['ï','ÂµL','â','_____________________']
myList = [word for word in myList if word not in exit]
#print(myList)
# POS tagging
tokens_pos = pos_tag(myList)
print(tokens_pos)
'''
with io.open(mainpath + "\\" + lonne + ".txt", 'w', encoding='utf-8') as f:  # save the results in file
    for item in myList:
        f.write("{}\n".format(item))
    # f.write(str(tokens_pos))


# search for reult of token from SNOMEDCT ontology
fnamev, file_extension = os.path.splitext(filenamemain)
mp = "C:\\Users\\Divya\\SOME\\" + fnamev
print(mp)
def make_sure_path_exists(path):
    os.makedirs(path, exist_ok=True)
make_sure_path_exists(mp)


mp = "C:\\Users\\Divya\\Desktop\\EHRR"
for i in myList:
    jj = SNOMEDCT.search(i)  # the  datatype of jj is snomedct type
    with io.open(mp + "\\" + str(i) + ".txt", 'w', encoding='utf-8') as f:  # save the results in file
        f.write(str(jj) + '\n')
print("donee")
'''

def ngrams(input, n):
    output = []
    for j in input:
        j = j.split(' ')
        if (len(j) < n):
            t = len(j)
            for i in range(len(j) - t + 1):
                output.append(j[i:i + t])
        else:
            for i in range(len(j) - n + 1):
                output.append(j[i:i + n])
    return output


count = 0
dirpath = "C:\\Users\\Divya\\Desktop\\EHRR"

#for i in tokens_pos[1:100]:  # postag of ehr tokens
pattern = tokens_pos[0]
#print(pattern[0])
#print(pattern[1])

'''
filename = "Patient.txt"
fname, file_extension = os.path.splitext(filename)
print(fname)
if fname == pattern[0]:
    with open("C:\\Users\\Divya\\Desktop\\EHRR\\" + filename) as f:
        lines = [line for line in f.readlines()]  # read lines from file
        #print(lines)

    for line in lines:
        count = count + 1
        #print(str(line))
        print("\n")
        tokenizer = RegexpTokenizer(r'\w+')
        tokens = tokenizer.tokenize(line)
        # tokenize line
        #print(tokens)
        tpos = pos_tag(tokens)  # pos tag of results
        #print(tpos)
        for j in tpos:
            # find our token
            if pattern[0] == j[0]:
                if j[1] != pattern[1]:
                    print(str(line))
                    lines.remove(line)

    print(count)
'''

pattern = tokens_pos[0:10]
patt = pattern[0]
tokenindex = pattern.index(pattern[0])
#print(patt[0])
lines = ['SNOMEDCT[913000]  # Chiropractic patient education (procedure)', 'SNOMEDCT[1889001]  # Patient transfer, in-hospital, unit-to-unit (procedure)', 'SNOMEDCT[1917008]  # Patient discharge, deceased, medicolegal case (procedure)'
, 'SNOMEDCT[1944003]  # Coagulation factor X Patient variant (substance)', 'SNOMEDCT[3133002]  # Patient discharge, deceased, autopsy (procedure)', 'SNOMEDCT[3286006]  # Patient status determination, greatly improved (finding)'
,' SNOMEDCT[3457005]  # Patient referral (procedure)'
, 'SNOMEDCT[3780001]  # Routine patient disposition, no follow-up planned (procedure)'
, 'SNOMEDCT[4525004]  # Emergency department patient visit (procedure)'
, 'SNOMEDCT[4266003]  # Patient referral for drug addiction rehabilitation (procedure)'
, 'SNOMEDCT[3929005]  # Patient transfer, in-hospital, bed-to-bed (procedure)'
, 'SNOMEDCT[5042005]  # Patient scale, device (physical object)'
, 'SNOMEDCT[6143009]  # Diabetic education (procedure)']
line = "SNOMEDCT[913000]  # Chiropractic patient education (procedure)"
tokenizer = RegexpTokenizer(r'\w+')
tokens = tokenizer.tokenize(line)  # tokenize line
tpos = pos_tag(tokens)  # pos tag of results
content_tokens = ngrams(lines, 5)
print(content_tokens)
#print(tpos)
#print(content_tokens[0])
flag = 0
score = 0
#print(pattern[0][1])



for tokenline in content_tokens:
    score = 0
    for item in tokenline:
        #print(item)
        if patt[0] == item:
            print("match")
            #print(tokenindex)
            itemindex = tokenline.index(item)
            flag = 1
            #print("\n")
            #print(itemindex)
            if flag == 1:
                print("flag1")
                litemindex = itemindex - 1  # left
                ltokenindex = tokenindex - 1  # left
                ritemindex = itemindex + 1  # right
                rtokenindex = tokenindex + 1  # right
                if litemindex < 0:
                    litemindex = itemindex
                if ltokenindex < 0:
                    ltokenindex = tokenindex
                if ritemindex > len(tokenline)-1:
                    ritemindex = itemindex
                if rtokenindex > len(pattern):
                    rtokenindex = tokenindex
                print(pattern[rtokenindex][0])
                print(tokenline[ritemindex])
                if tokenline[litemindex] == pattern[ltokenindex][0]:
                    score = score + 1
                if pattern[rtokenindex][0] == tokenline[ritemindex]:
                    score = score + 1
                if pattern[rtokenindex][0] == tokenline[ritemindex] and tokenline[litemindex] == pattern[ltokenindex][0]:
                    score = score + 2
    #print(score)
                print(tokenline)
                print("\n")
                if score > 0 and score < 2:
                    print(score)
                with io.open("C:\\Users\\Divya\\Desktop\\EHRDATA RELATED FILES\\jesuobso\\" + str(pattern[0]) + ".txt", 'w',encoding='utf-8') as f:  # save the results in file
                    f.write(str(tokenline))
                    print("one side match")
                if score > 2:
                    print(score)
                    print("two side match")




'''

        if pattern[0] == item:
            print('match')
            itemindex = tokenline.index(item)
            flag = 1
            print("\n")
            print(itemindex)


pattern = tokens_pos[0]
tokenindex = tokens_pos.index(pattern)
print(tokenindex)
print(pattern)
fname, file_extension = os.path.splitext(filename)
if fname == pattern[0]:
    with open("C:\\Users\\Divya\\Desktop\\EHRR\\" + filename) as f:
        lines = [line for line in f.readlines()]  # read lines from file
        #print("OKK")
        for line in lines:
            tokenizer = RegexpTokenizer(r'\w+')
            tokens = tokenizer.tokenize(line)  # tokenize line
            tpos = pos_tag(tokens)  # pos tag of results
            content_tokens = ngrams(line, 5)  # contenttokens contain ngrams of length 5 or less
            flag = 0
            score = 1
            for tokenline in content_tokens:
                for item in tokenline:
                    if pattern[0] == item:
                        print('match')
                        itemindex = tokenline.index(item)
                        flag = 1
                        if flag == 1:
                            litemindex = itemindex - 1  # left
                            ltokenindex = tokenindex - 1  # left
                            ritemindex = itemindex + 1  # right
                            rtokenindex = tokenindex + 1  # right
                            # if tokens_pos[ltokenindex] == "" or tokenline[litemindex] == "":
                            # dldmm
                            # if tokens_pos[rtokenindex] == "": or tokenline[ritemindex] == "":
                            # kdmdl
                            if tokenline[litemindex] == tokens_pos[ltokenindex] or tokens_pos[rtokenindex] == tokenline[
                                ritemindex]:
                                score = score + 1
                            if tokens_pos[rtokenindex] == tokenline[ritemindex] and tokenline[litemindex] == tokens_pos[
                                ltokenindex]:
                                score = score + 2
        while (score < 3):
            lines.remove(line)
            with io.open("C:\\Users\\Divya\\Desktop\\EHRDATA RELATED FILES\\jesuobso\\" + str(i[0]) + ".txt", 'w',
                         encoding='utf-8') as f:  # save the results in file
                f.write(str(lines) + '\n')
                # break
'''