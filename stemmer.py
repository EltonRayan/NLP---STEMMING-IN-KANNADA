# -*- coding: utf-8 -*-

import codecs
import re

f=codecs.open("kannada.txt",encoding='utf-8')
text=f.read()

#print(text.split(' '))

text=re.sub(r'(\d+)',r'',text)
text=text.replace(u',',' ')
text=text.replace(u'"',' ')
text=text.replace(u'(',' ')
text=text.replace(u')',' ')
text=text.replace(u'"',' ')
text=text.replace(u':',' ')
text=text.replace(u"'",' ')
text=text.replace(u"''",' ')
text=text.replace(u".",' ')
text=text.replace(u"*",' ')
text=text.replace(u"#",' ')
#print(sentences)
tokens=[]
tokens=text.split(' ')
#print(tokens)
#Tokenizing

for tok in tokens:
    tok=tok.strip()
    if tok == '':
        tokens.remove(tok)
print(tokens)

for each in tokens:
    if '-' in each:
        tok=each.split('-')
        tokens.remove(each)
        tokens.append(tok[0])
        tokens.append(tok[1])

#print(len(tokens))

#removing stop words


f=codecs.open("stopwords.txt",encoding='utf-8')
#tokens1=[]
stopwords=[x.strip() for x in f.readlines()]
tokens=[i for i in tokens if i not in stopwords]
#final_tokens=tokens
print(tokens)
#print(len(tokens))

#removing suffixes


suffixes={
               1:[u"ಗೆ",u"ವು",u"ವೇ",u"ಏ",u"ಲು",u"ಯು",u"ಸು"],
               2:[u"ಕ್ಕೆ",u"ನೇ",u"ದಿಸಿ",u"ನ್ನಲ್ಲಿ",u"ವಿಸಿ",u"ನಿಗೆ",u"ಇಗೆ",u"ಇನ",u"ತ್ತದೆ"],
               3:[u"ನಿಂದ",u"ನನ್ನು",u"ಯನ್ನು",u"ನನ್ನ",u"ವನ್ನ",u"ಗಳನ್ನು",u"ವನ್ನು",u"ದಲ್ಲಿ",u"ದಿಂದ",u"ದ್ದಾರೆ",u"ಇಂದ",u"ಅಧಿಕ",u"ಗಳು"],
               4:[u"ಇನಿಂದ",u"ಇನಲ್ಲಿ" ]
               }

stems=[]
for word in tokens:
    top=""
    temp=word
    for L in 4,3,2,1:
        #if len(word)>L:
            for suf in suffixes[L]:
                #print(type(suf),type(word),word,suf) 
                if word.endswith(suf):

                     word=word[:-len(suf)]
                     top=top+ word + u" \u002B " + suf
                if word.startswith(suf): 
                    word=word[L+1:]
                    if top =="":
                        top+=suf + u" \u002B " + word
                    else:
                        top= suf + u" \u002B " + top
                    break    
    if top:
        stems.append(top)
 
filename='stems_generated.txt'
f=codecs.open(filename,"w",encoding='utf-8')
for stem in stems: 
        #print(stem)
        f.write(stem)
        f.write(u"\u000D")
f.close()                
                    









