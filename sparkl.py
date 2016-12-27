import pymedtermino
pymedtermino.LANGUAGE = "en"
pymedtermino.REMOVE_SUPPRESSED_CONCEPTS = True

from pymedtermino import *
from pymedtermino.snomedct import *
from nltk import pos_tag

print("ok")
concept = SNOMEDCT[23689006]
print(concept)
print(concept.terms)

jj = SNOMEDCT.search("platelet")


dt_tags = [t for t in tokens_pos if t[1] == "NNP"]
print(dt_tags)

#print(jj)
print(concept.parents)
print(concept.children)

for ancestor in concept.ancestors(): print(ancestor)
list(concept.ancestors())
list(concept.descendants())

print("OK")
print(concept.relations)