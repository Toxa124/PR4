with open("words.txt", "r",encoding="utf-8") as f:
   string=  f.read()
   string=string.split()

def inRu(enWord):
   switch = {"VERB": "Глагол",
             "NOUN": "Существительное",
             "PREP": "Предлог",
             "INTJ": "Междометие"}
   return switch[enWord]

import pymorphy2
morph = pymorphy2.MorphAnalyzer()

for i,word in enumerate(string):
    a=morph.parse(word)[0]
    string[i] = word + " = " + inRu(a.tag.POS)

for a in string:
    print(a)

print("Версия для тестирования JetBrains")