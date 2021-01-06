import spacy

import sys
# parse command line
if file_name_given:
    inf = open(file_name_given)
else:
    inf = sys.stdin

nlp = spacy.load("en_core_web_sm")

introduction_text = open(inf).read()
introduction_doc = nlp(introduction_text)


for token in introduction_doc:
  if (token.pos_ == "PROPN" or token.pos_ == "NUM"):
    print(token)
