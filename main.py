with open("words.txt", "r",encoding="utf-8") as f:
   string=  f.read()
   string=string.split()

def in_ru(en_word):
   switch = {"VERB": "Глагол",
             "NOUN": "Существительное",
             "PREP": "Предлог",
             "INTJ": "Междометие"}
   return switch[en_word]

import pymorphy2
morph = pymorphy2.MorphAnalyzer()

for i,word in enumerate(string):
    a=morph.parse(word)[0]
    string[i] = word + " = " + in_ru(a.tag.POS)

for a in string:
    print(a)

print("Версия для тестирования JetBrains")