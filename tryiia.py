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
mainpath="C:\Users\Divya\Desktop\FILES\AVERAGE"

#OUTER MOST FOR LOOP
for filenamemain in os.listdir(mainpath):
    file_object = open(mainpath+filenamemain)
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
    mp="C:\\Users\\Divya\\"+filenamemain
    def make_sure_path_exists(mp):
        try:
            os.makedirs(mp)
        except OSError as exception:
            if exception.errno != errno.EEXIST:
                raise
    for i in myList:
        jj = SNOMEDCT.search(i) #the  datatype of jj is snomedct type
        with io.open(mp + "\\" + str(i) + ".txt", 'w', encoding='utf-8') as f: #save the results in file
            f.write(str(jj)+'\n')

    print("ok")


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
    dirpath = "C:\\Users\\Divya\\Desktop\\search"


    for i in tokens_pos[1:100]: #postag of ehr tokens
        pattern = i[0]
        print(pattern)
        pattpos = i[1]
        for filename in os.listdir(dirpath):
            fname, file_extension = os.path.splitext(filename)
            if fname == pattern:
                with open("C:\\Users\\Divya\\Desktop\\search\\" + filename) as f:
                    lines = [line for line in f.readlines()]  # read lines from file
                    # print("OKK")
                for line in lines:
                    tokenizer = RegexpTokenizer(r'\w+')
                    tokens = tokenizer.tokenize(line)  # tokenize line
                    tpos = pos_tag(tokens)  # pos tag of results
                    # print(tokens_pos)
                    for j in tpos:
                        # find our token
                        while (pattern == j[0]):
                            if j[1] != pattpos:
                                lines.remove(line)
                                print(filename)
                with io.open("C:\\Users\\Divya\\Desktop\\linerems\\" + str(i[0]) + ".txt", 'w', encoding='utf-8') as f:  # save the results in file
                    f.write(str(lines) + '\n')

    for i in tokens_pos:  # in  file with filename i
        tokenindex = tokens_pos.index(i)
        pattern = i[0]
        print(pattern)
        pattpos = i[1]
        for filename in os.listdir(dirpath):
            fname, file_extension = os.path.splitext(filename)
            if fname == pattern:
                with open("C:\\Users\\Divya\\Desktop\\search\\" + filename) as f:
                    lines = [line for line in f.readlines()]  # read lines from file
                    # print("OKK")
                for line in lines:
                    tokenizer = RegexpTokenizer(r'\w+')
                    tokens = tokenizer.tokenize(line)  # tokenize line
                    tpos = pos_tag(tokens)  # pos tag of results
                    content_tokens = ngrams(line, 5)  # contenttokens contain ngrams of length 5 or less
                    flag = 0
                    score = 1
                    for tokenline in content_tokens:
                        for item in tokenline:
                            if pattern == item:
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
                                    if tokenline[litemindex] == tokens_pos[ltokenindex]:
                                        score = score + 1
                                    if tokens_pos[rtokenindex] == tokenline[ritemindex]:
                                        score = score + 1
                                else:
                            # break






                                    ##REMOVE NUMBERS AND IF POSSIBLE NO AGE REMOVAL